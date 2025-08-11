param([string]$project="01-basics-calculator", [string]$file="calculator.py")
$path = Join-Path -Path $PSScriptRoot -ChildPath "..\projects\$project\$file"
python $path
