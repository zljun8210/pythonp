setlocal enabledelayedexpansion
@echo off
echo Input the PID
set /p id=PID is:
echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% > %id%.txt

:p
for /f "skip=3 tokens=5 delims= " %%a in ('tasklist /fi "pid eq %id%"') do (echo %%a 
@echo %%a>>%id%.txt
ping -n 2 127.0.0.1>nul)

echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% >> %id%.txt
goto p

  