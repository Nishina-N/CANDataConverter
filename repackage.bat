@echo off
REM =====================================
REM Repackage CANDataConverter
REM =====================================
echo.
echo Repackaging CANDataConverter v2.01...
echo.

REM Copy README_BINARY.txt to package
copy README_BINARY.txt dist\CANDataConverter_Package\

REM Remove old ZIP
if exist dist\CANDataConverter_v2.01_win64.zip del dist\CANDataConverter_v2.01_win64.zip

REM Create new ZIP
echo Creating ZIP file...
powershell -Command "Compress-Archive -Path 'dist\CANDataConverter_Package\*' -DestinationPath 'dist\CANDataConverter_v2.01_win64.zip' -Force"

echo.
echo =====================================
echo Repackage Complete!
echo =====================================
echo ZIP file: dist\CANDataConverter_v2.01_win64.zip
echo.

REM Show what's inside
echo Package contents:
dir /b dist\CANDataConverter_Package

echo.
pause
