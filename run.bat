@echo off
REM Wrapper to run a python script using the project's .venv if present.
REM Usage from cmd or PowerShell:
REM   run.bat "exercicio sql.py" arg1 arg2

nSET ROOT=%~dp0
nSET VENV=%ROOT%.venv\Scripts\python.exe

nIF EXIST "%VENV%" (
  "%VENV%" %*
) ELSE (
  python %*
)
ENDLOCAL