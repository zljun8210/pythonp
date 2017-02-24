@echo off & 
setlocal ENABLEDELAYEDEXPANSION
set t=3
set l=0
echo Input source file name
set /p name=source name :

echo Input target file name
set /p tn= target name:
echo  time    mem    CPU  > %tn%.txt
(for /f %%a in (%name%.txt) do (    
    set /p=%%a <nul
    set /a l +=1
    set /a m=!l!%%!t!
    if "!m!"=="0" echo. 
    )
) >> %tn%.txt
echo     Display the txt
type %tn%.txt
pause
    