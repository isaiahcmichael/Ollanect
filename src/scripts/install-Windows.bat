@echo off
echo "Installing Ollanect for Windows"

set "ollanectInstall=C:\Program Files\Ollanect"
md "C:\Program Files\Ollanect"
COPY ./ollanect.py "C:\Program Files\Ollanect\ollanect.py"
COPY ./setup-Windows.bat "C:\Program Files\Ollanect\ollanectSetupWindows.bat"
COPY ./LICENSE "C:\Program Files\Ollanect\ollanect-LICENSE"
setx /M PATH "%PATH%;%ollanectInstall%"

python --version >nul 2>nul
if %errorlevel%==0 (
    echo "Ollanect is installed!"
) else (
    echo "Ollanect is installed, but a version of Python was not found!"
)
pause