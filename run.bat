@echo off

setlocal enableextensions enabledelayedexpansion

set script_path=%~dp0
set script_path=%script_path:~0,-1%

:loop
tasklist /nh /fi "imagename eq python.exe" | find /i "server.py" > nul
if not errorlevel 1 (
    for /f "tokens=2" %%a in ('tasklist /fi "imagename eq python.exe" /fi "windowtitle eq %script_path:~2%" /fo list ^| find "PID:"') do set "pid=%%a"
    echo Server is running with PID %pid%, killing process...
    taskkill /f /pid %pid% > nul
)
echo Starting server...
start /b "" pythonw %script_path%\server.py >> %script_path%\log.txt 2>&1
timeout /t 5 > nul
goto loop
