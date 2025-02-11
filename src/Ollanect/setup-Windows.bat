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
echo. > "%configDir%\serverInfo.txt"

set /p ServerHTTPS=Is your Ollama Server using HTTPS? (y/N)
if "%ServerHTTPS%"=="y" set ServerHTTPS="https://"
if "%ServerHTTPS%"=="Y" set ServerHTTPS="https://"
if "%ServerHTTPS%"=="n" set ServerHTTPS="http://"
if "%ServerHTTPS%"=="N" set ServerHTTPS="http://"
if "%ServerHTTPS%"=="" set ServerHTTPS="http://"
if "%ServerHTTPS%"==" " set ServerHTTPS="http://"

set /p ServerURL=What is your Ollama Server URL (Do not include port and HTTP)? 

set /p ServerPort=What is the port of your Server? (The default port is 11434)? 
if "%ServerPort%"=="" set ServerPort=11434
if "%ServerPort%"==" " set ServerPort=11434

echo %ServerHTTPS%%ServerURL%:%ServerPort%> "%configDir%\serverInfo.txt"

echo Complete!
python "%~dp0ollanect.py"

:: End of Ollanect File.