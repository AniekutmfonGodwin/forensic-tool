@echo off
SETLOCAL DisableDelayedExpansion

SETLOCAL
for %%a in (1) do (
    set "prompt=$_"
    echo on
    for %%b in (1) do rem * #%*#
    @echo off
) > argv.txt
ENDLOCAL

for /F "delims=" %%L in (argv.txt) do (
  set "argv=%%L"
)
SETLOCAL EnableDelayedExpansion
set "argv=!argv:*#=!"
set "argv=!argv:~0,-2!"
REM argv now contains the unmodified content of %* .

python file_analyser !argv!