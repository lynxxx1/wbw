title HEAVEN - Installation of modules.
@echo off
cls
echo Installing the python modules required for the HEAVEN Tool:
timeout /t 5 /nobreak > nul
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
timeout /t 5 /nobreak > nul
pip install time
pip install selenium
pip install colorama
pip install requests
pip install json
pip install random
pip install string
pip install ctypes
pip install base64
pip install threading
pip install psutil
pip install bs4
pip install webbrowser
pip install itertools
pip install phonenumbers
pip install discord
pip install discord.py
pip install PyQt5
pip install PyQtWebEngine
echo Finish.
timeout /t 5 /nobreak > nul
start Start.bat
