"""
Command-line interface for YouTube Downloader Pro.
"""
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from src.downloader import DownloadConfig, VideoFormat, VideoQuality, YouTubeDownloader

app = typer.Typer(
    name="youtube-dl-pro",
    help="A professional YouTube video and playlist downloader with quality selection.",
    add_completion=False,
)
console = Console()

def display_header():
    """Display application header."""
    console.print(
        Panel.fit(
            "[bold cyan]YouTube Downloader Pro[/]\n"
            "[dim]Download videos and playlists with custom quality[/]",
            border_style="cyan",
        )
    )

def validate_url(url: str) -> bool:
    """Basic URL validation."""
    return any(domain in url for domain in ["youtube.com/watch?v=", "youtu.be/"])

@app.command()
def download(
    url: str = typer.Argument(..., help="YouTube video or playlist URL"),
    format: VideoFormat = typer.Option(
        VideoFormat.MP4,
        "--format", "-f",
        help="Output format (mp4 or mp3)",
    ),
    quality: VideoQuality = typer.Option(
        VideoQuality.HIGHEST,
        "--quality", "-q",
        help="Video quality (144p to 1080p, or 'highest'/'lowest')",
    ),
    output: Path = typer.Option(
        Path("downloads"),
        "--output", "-o",
        help="Output directory for downloaded files",
    ),
    skip_existing: bool = typer.Option(
        False,
        "--skip-existing", "-s",
        help="Skip downloading if file already exists",
    ),
):
    """Download a video or playlist from YouTube."""
    display_header()

    if not validate_url(url):
        console.print("[bold red]Error:[/] Invalid YouTube URL")
        raise typer.Exit(1)

    config = DownloadConfig(
        output_path=output,
        format=format,
        quality=quality,
        skip_existing=skip_existing,
    )

    downloader = YouTubeDownloader(config)

    if "playlist" in url:
        downloader.download_playlist(url)
    else:
        downloader.download_video(url)

@app.command()
def version():
    """Display version information."""
    from src import __version__
    console.print(f"YouTube Downloader Pro v{__version__}")

def main():
    """Main entry point."""
    app()