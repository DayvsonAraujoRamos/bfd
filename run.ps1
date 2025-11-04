<#
Small helper to run a Python script from the project using the project's venv if present.
Usage (PowerShell):
    ./run.ps1 .\"exercicio sql.py\" -- arg1 arg2

This script does NOT change system state. To allow running this script you may need
to temporarily relax execution policy for the current session:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

#>
param(
    [Parameter(Mandatory=$true, Position=0)] [string]$ScriptPath,
    [Parameter(ValueFromRemainingArguments=$true)] [string[]]$ScriptArgs
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $root '.venv\Scripts\python.exe'

if (Test-Path $venvPython) {
    Write-Host "Using venv python: $venvPython"
    & $venvPython $ScriptPath @ScriptArgs
} else {
    Write-Host "Using system 'python' (no .venv found)"
    & python $ScriptPath @ScriptArgs
}