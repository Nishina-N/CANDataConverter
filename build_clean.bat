@echo off
REM =====================================
REM CANDataConverter Clean Build
REM (with Virtual Environment)
REM =====================================
echo.

REM Virtual environment name
set VENV_NAME=venv_build

REM Remove old virtual environment
if exist %VENV_NAME% (
    echo Removing old virtual environment...
    rmdir /s /q %VENV_NAME%
)

REM Create new virtual environment
echo Creating virtual environment...
python -m venv %VENV_NAME%

REM Activate virtual environment
echo Activating virtual environment...
call %VENV_NAME%\Scripts\activate.bat

REM Install required packages only
echo.
echo Installing required packages only...
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

REM Show installed packages
echo.
echo Installed packages:
pip list

REM Cleanup
echo.
echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
if exist tool\__pycache__ rmdir /s /q tool\__pycache__

REM Build executable
echo.
echo Building executable...
pyinstaller CANDataConverter.spec

REM Check result
if exist dist\CANDataConverter.exe (
    echo.
    echo =====================================
    echo Build SUCCESS!
    echo =====================================
    echo Executable: dist\CANDataConverter.exe
    
    REM Show file size
    for %%I in (dist\CANDataConverter.exe) do (
        set /a SIZE_MB=%%~zI / 1048576
        echo File size: %%~zI bytes ^(approx. !SIZE_MB! MB^)
    )
    echo.
    
    REM Create distribution package
    echo Creating distribution package...
    if not exist dist\CANDataConverter_Package mkdir dist\CANDataConverter_Package
    copy dist\CANDataConverter.exe dist\CANDataConverter_Package\
    copy README_BINARY.txt dist\CANDataConverter_Package\
    copy LICENSE dist\CANDataConverter_Package\
    if exist ico xcopy ico dist\CANDataConverter_Package\ico\ /E /I /Y
    
    echo.
    echo Package created: dist\CANDataConverter_Package\
    echo.
    
    REM Create ZIP file using PowerShell
    echo Creating ZIP file...
    powershell -Command "Compress-Archive -Path 'dist\CANDataConverter_Package\*' -DestinationPath 'dist\CANDataConverter_v2.01_win64.zip' -Force"
    echo ZIP created: dist\CANDataConverter_v2.01_win64.zip
    echo.
) else (
    echo.
    echo =====================================
    echo Build FAILED
    echo =====================================
    echo Please check the error messages above
    echo.
)

REM Deactivate virtual environment
call %VENV_NAME%\Scripts\deactivate.bat

echo.
echo Build process completed!
echo Virtual environment: %VENV_NAME%
echo.
pause
