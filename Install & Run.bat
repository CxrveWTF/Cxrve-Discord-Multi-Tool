@echo off
echo Installing required dependencies...

:: Install dependencies from requirements.txt
pip install -r requirements.txt

echo Installation complete.

:: Now, running the Discord Multi-Tool executable
echo Running Discord-Multi-Tool.exe...
start "" "Discord-Multi-Tool.exe"

pause
