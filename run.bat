@echo off

set port=9000

:loop
for /f "tokens=2" %%a in ('netstat -aon ^| findstr :%port% ^| findstr LISTENING') do set PID=%%a

if not "%PID%"=="" (
    echo Server is already running with PID %PID%. Killing process...
    taskkill /F /PID %PID%
    timeout /t 5 >nul
) else (
    echo Starting server...
    start /b pythonw server.py >> log.txt 2>&1
)

goto loop
