@echo off
:main
cls
python main.py
timeout /t 3>nul
goto main