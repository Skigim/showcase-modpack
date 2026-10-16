@echo off
rem Links this pack's mods into RSMM's mods folder (see tools\link_mods.py).
python "%~dp0tools\link_mods.py" %*
echo.
pause
