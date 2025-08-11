# 📋 PyBuildExePathExample

This project demonstrates how different Python path-related variables and functions behave when running a Python script directly versus when the script is compiled into an executable using **PyInstaller** or **Nuitka**. The example highlights the differences in `__file__`, `sys.argv[0]`, `sys.path`, `Path.cwd()`, `os.getcwd()`, and `sys.executable` in these scenarios.

## 📂 Project Structure

- `app.py`: The main Python script that outputs various path-related information.
- `build.pyinstaller.bat`: Batch script to compile `app.py` into a single executable using **PyInstaller**.
- `build.nuitka.bat`: Batch script to compile `app.py` into a single executable using **Nuitka**.
- `pizza.png` 🍕: Image file used for the compiled executables' icon.

## ✅ Prerequisites

- **Python 3.12** installed (ensure `python` is available in your system PATH).
- **PyInstaller**: Install via `pip install pyinstaller`.
- **Nuitka**: Install via `pip install nuitka`.
- A `pizza.png` 🍕 file in the project directory for the executable icon.

## 🚀 Usage

### ▶️ Running the Script Directly

Execute `app.py` using **Python** to see the path-related outputs:

```bash
python app.py
```

**Expected Output**:

```
__file__       - D:\WorkSpace\~Demo\PyBuildExePathExample\app.py
sys.argv[0]    - D:\WorkSpace\~Demo\PyBuildExePathExample\app.py
sys.path[0]    - D:\WorkSpace\~Demo\PyBuildExePathExample
sys.path[1]    - C:\Python\Python312\python312.zip
Path.cwd()     - D:\WorkSpace\~Demo\PyBuildExePathExample
os.getcwd()    - D:\WorkSpace\~Demo\PyBuildExePathExample
sys.executable - C:\Python\Python312\python.exe
```

### 🛠️ Building with PyInstaller

Run the **PyInstaller** batch script to compile `app.py` into a single executable:

```bash
build.pyinstaller.bat
```

This executes:

```bash
pyinstaller --onefile --icon=pizza.png app.py
```

The compiled executable will be located in the `dist` folder (`dist\app.exe`). Run the executable:

```bash
dist\app.exe
```

**Expected Output**:

```
__file__       - D:\Temp\_MEI42762\app.py
sys.argv[0]    - D:\WorkSpace\~Demo\PyBuildExePathExample\dist\app.exe
sys.path[0]    - D:\Temp\_MEI42762\base_library.zip
sys.path[1]    - D:\Temp\_MEI42762\lib-dynload
Path.cwd()     - D:\WorkSpace\~Demo\PyBuildExePathExample\dist
os.getcwd()    - D:\WorkSpace\~Demo\PyBuildExePathExample\dist
sys.executable - D:\WorkSpace\~Demo\PyBuildExePathExample\dist\app.exe
```

### 🛠️ Building with Nuitka

Run the **Nuitka** batch script to compile `app.py` into a single executable:

```bash
build.nuitka.bat
```

This executes:

```bash
nuitka --onefile --standalone --lto=yes --follow-imports --show-progress --windows-icon-from-ico=pizza.png app.py
```

The compiled executable will be `app.exe` in the project directory. Run the executable:

```bash
app.exe
```

**Expected Output**:

```
__file__       - D:\Temp\onefile_17188_133989983771239187\app.py
sys.argv[0]    - D:\WorkSpace\~Demo\PyBuildExePathExample\app.exe
sys.path[0]    - D:\WorkSpace\~Demo\PyBuildExePathExample
sys.path[1]    - D:\WorkSpace\~Demo\PyBuildExePathExample
Path.cwd()     - D:\WorkSpace\~Demo\PyBuildExePathExample
os.getcwd()    - D:\WorkSpace\~Demo\PyBuildExePathExample
sys.executable - D:\WorkSpace\~Demo\PyBuildExePathExample\app.exe
```

### 📊 Comparison of Path Variables

The following compares the path-related variables across the three execution scenarios based on the expected outputs:

```
Compare 
Direct Python Script - python app.py
PyInstaller Executable - dist\app.exe
Nuitka Executable - app.exe

__file__
D:\WorkSpace\~Demo\PyBuildExePathExample\app.py
D:\Temp\_MEI42762\app.py 
D:\Temp\onefile_17188_133989983771239187\app.py

⭐sys.argv[0]⭐
D:\WorkSpace\~Demo\PyBuildExePathExample\app.py
D:\WorkSpace\~Demo\PyBuildExePathExample\dist\app.exe
D:\WorkSpace\~Demo\PyBuildExePathExample\app.exe

sys.path[0]
D:\WorkSpace\~Demo\PyBuildExePathExample
D:\Temp\_MEI42762\base_library.zip
D:\WorkSpace\~Demo\PyBuildExePathExample

sys.path[1]
C:\Python\Python312\python312.zip
D:\Temp\_MEI42762\lib-dynload
D:\WorkSpace\~Demo\PyBuildExePathExample

⭐Path.cwd()⭐
D:\WorkSpace\~Demo\PyBuildExePathExample
D:\WorkSpace\~Demo\PyBuildExePathExample\dist
D:\WorkSpace\~Demo\PyBuildExePathExample

⭐os.getcwd()⭐
D:\WorkSpace\~Demo\PyBuildExePathExample
D:\WorkSpace\~Demo\PyBuildExePathExample\dist
D:\WorkSpace\~Demo\PyBuildExePathExample

sys.executable
C:\Python\Python312\python.exe
D:\WorkSpace\~Demo\PyBuildExePathExample\dist\app.exe
D:\WorkSpace\~Demo\PyBuildExePathExample\app.exe
```

## 📝 Notes

- **PyInstaller**: The executable unpacks to a temporary directory (e.g., `D:\Temp\_MEI42762`), which affects `__file__` and `sys.path[0]`. The current working directory reflects the `dist` folder.
- **Nuitka**: The executable maintains the project directory in `sys.path` and uses a temporary directory for `__file__`. The current working directory remains the project directory.
- Ensure the `pizza.png` 🍕 file exists in the project directory before building to avoid errors.
- The temporary directories (e.g., `D:\Temp\_MEI42762` for **PyInstaller** or `D:\Temp\onefile_17188_...` for **Nuitka**) are created at runtime and may vary.

## 📜 License

This project is provided as-is for demonstration purposes. No License is applied.

## 🤖 Generated by Grok

This README was generated by **Grok**, created by **xAI**.