@echo off

:loop
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :9000 ^| findstr LISTENING') do set PID=%%a

if not "%PID%"=="" (
    echo Server is already running with PID %PID%.
    timeout /t 5 >nul
) else (
    echo Starting server...
    start /b pythonw server.py >> log.txt 2>&1
)

goto loop
