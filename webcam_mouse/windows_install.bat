@echo OFF

:: Last modified on 02/16/17 by Timothy Lock

reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT

:: Python 2.7.5 Install
echo Installing Python 2.7.13
msiexec /i "%~dp0\install\python-2.7.13.msi" /qb!
echo Done
echo .
echo .

:: Install OpenCV
echo Installing OpenCV
copy "%~dp0\install\opencv\x86\cv2.pyd" "C:\Python27\Lib\site-packages"
echo Done
echo .
echo .

:: Install Libraries
echo Installing Python Libraries
"C:\Python27\Scripts\pip2.exe" install -U numpy
"C:\Python27\Scripts\pip2.exe" install -U pyautogui
echo Done
echo .
echo .

:: Finish
pause