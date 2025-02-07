@echo off
echo This is the setup for Ollanect

set "configDir=%APPDATA%\Ollanect"
mkdir "%configDir%" 2>nul
echo. > "%configDir%\serverInfo.txt"

set /p ServerURL=What is your Ollama Server URL (Do not include port and HTTP)? 

set /p ServerPort=What is the port of your Server? (The default port is 11434)? 
if "%ServerPort%"=="" set ServerPort=11434
if "%ServerPort%"==" " set ServerPort=11434

echo %ServerURL%:%ServerPort%> "%configDir%\serverInfo.txt"

echo Complete!
python "%~dp0ollanect.py"