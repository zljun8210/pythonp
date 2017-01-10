setlocal enabledelayedexpansion
@echo off
set var=0
echo Input the PID
set /p id=PID is:
echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% > %id%.txt

:p
for /f "skip=1 tokens=2 delims==" %%a in ('wmic process where "processid='%id%'" get workingsetsize /value') do ( 
@echo %%a
set /a var=%%a/1024)
@echo %var% K
@echo %var% >> %id%.txt

ping -n 60 127.0.0.1>nul
echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% >> %id%.txt
goto p

  