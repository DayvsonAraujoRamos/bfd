Enable running Python scripts in this project

This project includes two small wrappers to run Python scripts using the project's
virtual environment (.venv) if present.

Files added:
- run.ps1  — PowerShell wrapper. Usage:
    # (optional) allow script execution in this PowerShell session
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

    # run a script
    ./run.ps1 "exercicio sql.py"

- run.bat  — Windows CMD/batch wrapper. Usage:
    run.bat "exercicio sql.py"

Behavior:
- If a `.venv` folder exists in the project root (the common venv created by the
  environment tools), the wrappers will call `.venv\Scripts\python.exe`.
- Otherwise they call the system `python` found in PATH.

Security notes:
- The wrappers do not change your system settings or the database.
- If you need to run PowerShell scripts, setting execution policy to `Bypass` for
  the current process is safe and temporary:
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

If you want, I can also:
- add an association so double-clicking `.py` files runs them with the venv python,
  or
- create small desktop shortcuts for common scripts.

Let me know which additional option you prefer.