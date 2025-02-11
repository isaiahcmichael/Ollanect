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

echo "Installing Ollanect for Windows"

set "ollanectInstall=C:\Program Files\Ollanect"
md "C:\Program Files\Ollanect"
COPY ollanect.py "C:\Program Files\Ollanect\ollanect.py"
COPY setup-Windows.bat "C:\Program Files\Ollanect\ollanectSetupWindows.bat"
COPY LICENSE "C:\Program Files\Ollanect\ollanect-LICENSE"
setx /M PATH "%PATH%;%ollanectInstall%"
pip install -r requirements.txt

python --version >nul 2>nul
if %errorlevel%==0 (
    echo "Ollanect is installed!"
) else (
    echo "Ollanect is installed, but a version of Python was not found!"
)
pause

:: End of Ollanect File.