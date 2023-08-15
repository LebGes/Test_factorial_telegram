@echo off

call %~dp0test_bot\venv\Scripts\activate

cd %~dp0test_bot

set TOKEN=6612863618:AAEtcSaCQwHCQwHwrXLwSI79GyACa7q6_tI

python test_bot.py

pause