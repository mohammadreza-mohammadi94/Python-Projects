"""
Core functionality for downloading YouTube videos and playlists using yt-dlp.
"""
from __future__ import annotations

import os
import math
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime

import yt_dlp
from pydantic import BaseModel
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
    DownloadColumn,
)

console = Console()

class VideoFormat(str, Enum):
    """Supported video formats."""
    MP4 = "mp4"
    MP3 = "mp3"

class VideoQuality(str, Enum):
    """Supported video qualities."""
    HIGHEST = "highest"
    LOWEST = "lowest"
    Q144P = "144p"
    Q240P = "240p"
    Q360P = "360p"
    Q480P = "480p"
    Q720P = "720p"
    Q1080P = "1080p"

class DownloadConfig(BaseModel):
    """Configuration for video download."""
    output_path: Path = Path("downloads")
    format: VideoFormat = VideoFormat.MP4
    quality: VideoQuality = VideoQuality.HIGHEST
    skip_existing: bool = False

class YouTubeDownloader:
    """Main downloader class for YouTube videos and playlists."""

    def __init__(self, config: Optional[DownloadConfig] = None):
        """Initialize downloader with configuration."""
        self.config = config or DownloadConfig()
        self.config.output_path.mkdir(parents=True, exist_ok=True)

    def _get_format(self) -> str:
        """Get the format string based on configuration."""
        if self.config.format == VideoFormat.MP3:
            return "bestaudio[ext=m4a]/bestaudio/best"
        
        if self.config.quality == VideoQuality.HIGHEST:
            return "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        elif self.config.quality == VideoQuality.LOWEST:
            return "worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst"
        else:
            # More specific format selection for better performance
            height = self.config.quality.value[:-1]  # Remove 'p' from quality
            return (f"bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/"
                   f"best[height<={height}][ext=mp4]/"
                   f"best[height<={height}]")

    def _get_output_template(self, is_playlist: bool = False) -> str:
        """Get the output template for yt-dlp."""
        if is_playlist:
            return str(self.config.output_path / "%(playlist_title)s" / "%(title)s.%(ext)s")
        return str(self.config.output_path / "%(title)s.%(ext)s")

    def _get_ydl_opts(self, is_playlist: bool = False) -> dict:
        """Get yt-dlp options based on configuration."""
        format_str = self._get_format()
        output_template = self._get_output_template(is_playlist)

        ydl_opts = {
            'format': format_str,
            'outtmpl': output_template,
            'quiet': True,
            'no_warnings': True,
            'progress_hooks': [self._progress_hook],
            'concurrent_fragments': 3,  # Download fragments concurrently
            'retries': 10,  # Retry on error
            'file_access_retries': 5,
            'fragment_retries': 10,
            'retry_sleep': lambda n: 5 * (n + 1),  # Exponential backoff
            'socket_timeout': 30,
        }

        if self.config.format == VideoFormat.MP3:
            ydl_opts.update({
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'postprocessor_args': [
                    '-threads', '4',  # Use 4 threads for conversion
                ],
            })

        return ydl_opts

    def _create_progress(self) -> Progress:
        """Create a rich progress bar."""
        return Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            "[progress.percentage]{task.percentage:>3.1f}%",
            "•",
            DownloadColumn(),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
            console=console,
            transient=True,
        )

    def _progress_hook(self, d: dict):
        """Progress hook for yt-dlp."""
        if not hasattr(self, '_progress'):
            self._progress = self._create_progress()
            self._task_id = None

        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            speed = d.get('speed', 0)
            if total > 0:
                if self._task_id is None:
                    with self._progress:
                        self._task_id = self._progress.add_task(
                            description=f"Downloading {d.get('info_dict', {}).get('title', 'video')}",
                            total=total,
                        )

                if hasattr(self, '_progress'):
                    self._progress.update(
                        self._task_id,
                        completed=downloaded,
                        refresh=True,
                    )

        elif d['status'] == 'finished':
            if hasattr(self, '_progress'):
                self._progress.stop()
                delattr(self, '_progress')
                self._task_id = None
            console.print("\n[bold green]Download completed.[/] Processing...")

    def _format_size(self, bytes: int) -> str:
        """Format bytes to human readable size."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes < 1024:
                return f"{bytes:.1f}{unit}"
            bytes /= 1024
        return f"{bytes:.1f}TB"

    def download_video(self, url: str) -> bool:
        """Download a single video."""
        try:
            console.print(f"[bold cyan]Fetching video information...[/]")
            
            opts = self._get_ydl_opts()
            opts['verbose'] = True  # Enable verbose output
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                try:
                    console.print("[bold cyan]Extracting video information...[/]")
                    info = ydl.extract_info(url, download=True)  # Changed to True to download directly
                    
                    if not info:
                        console.print("[bold red]Error:[/] Could not fetch video information")
                        return False
                    
                    console.print(f"[bold green]Download completed successfully![/]")
                    console.print(f"[bold cyan]Title:[/] {info.get('title', 'Unknown')}")
                    console.print(f"[bold cyan]Format:[/] {self.config.format.value.upper()}")
                    return True
                        
                except Exception as e:
                    console.print(f"[bold red]Download error:[/] {str(e)}")
                    return False
                    
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")
            return False

        except Exception as e:
            console.print(f"[bold red]Error downloading video:[/] {str(e)}")
            return False

    def download_playlist(self, url: str) -> bool:
        """Download all videos from a playlist."""
        try:
            console.print(f"[bold cyan]Fetching playlist information...[/]")
            
            with yt_dlp.YoutubeDL(self._get_ydl_opts(is_playlist=True)) as ydl:
                info = ydl.extract_info(url, download=False)
                if 'entries' not in info:
                    console.print("[bold red]Error:[/] Not a valid playlist URL")
                    return False

                console.print(f"[bold cyan]Playlist Title:[/] {info.get('title', 'Unknown')}")
                console.print(f"[bold cyan]Number of videos:[/] {len(info['entries'])}")
                
                console.print(f"[bold green]Starting downloads...[/]")
                ydl.download([url])
                console.print(f"\n[bold green]Successfully downloaded playlist![/]")
                return True

        except Exception as e:
            console.print(f"[bold red]Error downloading playlist:[/] {str(e)}")
            return False