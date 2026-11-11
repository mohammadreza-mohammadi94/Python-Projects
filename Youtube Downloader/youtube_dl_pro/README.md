# YouTube Downloader Pro

A professional-grade YouTube video and playlist downloader with quality selection, progress tracking, and format conversion capabilities.

## Features

- ✨ Download single videos or entire playlists
- 🎥 Support for multiple video qualities (144p to 1080p)
- 🎵 Convert videos to MP3 format
- 📊 Real-time progress tracking with progress bars
- 🎯 Skip existing files option
- 🎨 Beautiful CLI interface with rich formatting
- 💪 Type-safe implementation with error handling

## Project Structure

```
youtube_dl_pro/
├── .venv/              # Virtual environment directory
├── downloads/          # Default download directory
├── src/               # Source code directory
│   ├── __init__.py
│   ├── cli.py         # Command-line interface
│   └── downloader.py  # Core downloader functionality
├── pyproject.toml     # Project configuration and dependencies
├── requirements.txt   # Pinned dependencies
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd youtube_dl_pro
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On Unix/macOS:
source .venv/bin/activate
```

3. Install the package:

```bash
pip install -e .
```

## Usage

Make sure your virtual environment is activated before using the tool:

```bash
# On Windows:
.\.venv\Scripts\activate
# On Unix/macOS:
source .venv/bin/activate
```

### Download Commands

```bash
# Activate the virtual environment first
.\.venv\Scripts\activate

# Then use the commands
ytdl download "https://www.youtube.com/watch?v=VIDEO_ID" -f mp3
```

### Command Options

#### Download a Single Video

```bash
# Download with highest quality in MP4 format
ytdl download https://www.youtube.com/watch?v=VIDEO_ID

# Download in specific quality
ytdl download https://www.youtube.com/watch?v=VIDEO_ID -q 720p

# Download as MP3
ytdl download https://www.youtube.com/watch?v=VIDEO_ID -f mp3

# Specify output directory
ytdl download https://www.youtube.com/watch?v=VIDEO_ID -o /path/to/output

# Skip if file already exists
ytdl download https://www.youtube.com/watch?v=VIDEO_ID -s
```

### Download a Playlist

```bash
# Download all videos in a playlist
ytdl download https://www.youtube.com/playlist?list=PLAYLIST_ID

# Download playlist videos in specific quality
ytdl download https://www.youtube.com/playlist?list=PLAYLIST_ID -q 480p -f mp4
```

### Command-line Options

- `-f, --format [mp4|mp3]`: Output format (default: mp4)
- `-q, --quality [144p|240p|360p|480p|720p|1080p|highest|lowest]`: Video quality (default: highest)
- `-o, --output PATH`: Output directory (default: ./downloads)
- `-s, --skip-existing`: Skip downloading if file already exists

### Show Version

```bash
ytdl version
```

## Dependencies

Core dependencies:

- yt-dlp: Advanced YouTube video download functionality
- rich: Terminal formatting and progress bars
- typer: Command-line interface
- pydantic: Data validation
- moviepy: Video/audio conversion

Development dependencies:

- pytest: Testing framework
- black: Code formatting
- isort: Import sorting
- flake8: Code linting
- mypy: Type checking

## Development

1. Install development dependencies:

```bash
pip install -e ".[dev]"
```

2. Run tests:

```bash
pytest
```

3. Format code:

```bash
black .
isort .
```

4. Type checking:

```bash
mypy src
```

## Troubleshooting

1. **Command not found**: If `ytdl` command is not found after installation:

   - Make sure you've run `add_to_path.ps1`
   - Open a new terminal window
   - If still not working, manually add the project directory to your PATH

2. **Download errors**: If downloads fail:
   - Check your internet connection
   - Verify the video URL is accessible
   - Try with different quality settings
   - Make sure you have enough disk space

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
