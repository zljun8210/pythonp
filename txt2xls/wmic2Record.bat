@setlocal enabledelayedexpansion
@echo off
set var=0
::获取进程号
echo Input the PID
set /p id=PID is:
@echo.

::获取CPU的核心数
::echo Input CPU Logical Processor
::set /p cp=CPUS is:
::@echo.
for /f "skip=1 tokens=2 delims==" %%l in ('wmic cpu get numberofcores /value') do set /a cp=%%l
::@echo CPU is %cp% processor.
@echo.
echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% > %id%.txt

:p
for /f "skip=1 tokens=2 delims==" %%i in ('wmic path Win32_PerfFormattedData_PerfOS_Processor get PercentProcessorTime /value^|findstr "PercentProcessorTime"') do (
set /a Han+=%%i)
set /a Han/=%cp%

for /f "skip=1 tokens=2 delims==" %%a in ('wmic process where "processid='%id%'" get workingsetsize /value') do ( 
@echo %%a >> %id%.txt
set /a var=%%a/1024)
::set /a var=%var%/1024
@echo %var% KB


@echo %Han%%%
@echo %Han% >> %id%.txt

ping -n 5 127.0.0.1>nul
echo %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% >> %id%.txt
goto p

  