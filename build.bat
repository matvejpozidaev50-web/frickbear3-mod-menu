@echo off
REM Frickbear 3 Mod Menu - Simple EXE Builder
REM One command to build the executable!

echo.
echo ======================================================
echo Building Frickbear 3 Mod Menu EXE
echo ======================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Checking dependencies...
pip list | find "PyInstaller" >nul
if errorlevel 1 (
    echo Installing PyInstaller (this may take a minute)...
    pip install PyInstaller -q
)

pip list | find "PyYAML" >nul
if errorlevel 1 (
    echo Installing PyYAML...
    pip install PyYAML -q
)

REM Build
echo.
echo Building... This may take 1-2 minutes
echo.
python build_exe_simple.py

if errorlevel 1 (
    echo.
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ======================================================
echo BUILD COMPLETE!
echo ======================================================
echo.
echo Your EXE is ready at: dist\FrickbearModMenu.exe
echo.
pause
