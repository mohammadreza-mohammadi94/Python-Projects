@echo off
SET SCRIPT_DIR=%~dp0
call "%SCRIPT_DIR%.venv\Scripts\activate.bat" && ytdl %*