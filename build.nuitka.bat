:: Compile with Nuitka
nuitka --onefile --standalone --lto=yes --follow-imports --show-progress --windows-icon-from-ico=pizza.png app.py
IF %ERRORLEVEL% NEQ 0 (
    ECHO Build failed!
    pause
    exit /b 1
)