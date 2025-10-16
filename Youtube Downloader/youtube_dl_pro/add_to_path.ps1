# Get the directory containing the ytdl script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

# Add to PATH if not already there
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$scriptPath*") {
    [Environment]::SetEnvironmentVariable("Path", "$userPath;$scriptPath", "User")
    Write-Host "Added ytdl to your PATH. Please restart your terminal to use the 'ytdl' command from anywhere."
}
else {
    Write-Host "ytdl is already in your PATH."
}