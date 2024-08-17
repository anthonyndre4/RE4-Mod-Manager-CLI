@echo off
setlocal

for /f "delims=" %%i in ('make check-poetry') do set "output=%%i"

set "ifTrue=True"

if %output% == %ifTrue% (
    echo "Poetry is installed fine, nothing to do :)..."
) else (
    echo "Poetry is not configured correctly, installing now.."
    poetry install
)

endlocal
