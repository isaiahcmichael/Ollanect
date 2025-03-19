@echo off

:: This file is part of Ollanect.
::
:: Ollanect is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: Ollanect is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with Ollanect.  If not, see <http://www.gnu.org/licenses/>.

echo This is the setup for Ollanect

set "configDir=%APPDATA%\Ollanect"
mkdir "%configDir%" 2>nul

set "serverInfoFile=serverInfo.txt"

if "%~1"=="-2" (
    set "serverInfoFile=serverInfo-2.txt"
) else if "%~1"=="-3" (
    set "serverInfoFile=serverInfo-3.txt"
) else if "%~1"=="-4" (
    set "serverInfoFile=serverInfo-4.txt"
) else if "%~1"=="-5" (
    set "serverInfoFile=serverInfo-5.txt"
)

echo. > "%configDir%\%serverInfoFile%"

set /p ServerHTTPS=Is your Ollama Server using HTTPS? (y/N)
if /I "%ServerHTTPS%"=="y" set ServerHTTPS="https://"
if /I "%ServerHTTPS%"=="n" set ServerHTTPS="http://"
if "%ServerHTTPS%"=="" set ServerHTTPS="http://"
if "%ServerHTTPS%"==" " set ServerHTTPS="http://"

set /p ServerURL=What is your Ollama Server URL (Do not include port and HTTP)? 

set /p ServerPort=What is the port of your Server? (The default port is 11434)? 
if "%ServerPort%"=="" set ServerPort=11434
if "%ServerPort%"==" " set ServerPort=11434

echo %ServerHTTPS%%ServerURL%:%ServerPort%> "%configDir%\%serverInfoFile%"

echo Complete!
python "%~dp0ollanect.py" "%~1"

:: End of Ollanect File.