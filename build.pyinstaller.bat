:: Compile with PyInstaller
pyinstaller --onefile --icon=pizza.png app.py
IF %ERRORLEVEL% NEQ 0 (
    ECHO Build failed!
    pause
    exit /b 1
)