from cx_Freeze import setup, Executable
import sys
import sys
sys.argv.append("build")
base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [Executable("calculadora.py", base=base)] # Nome do Arquivo que contém seu código

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Calculadora",
    options = options,
    version = "5.0",
    description = 'create by Pedro',
    executables = executables
)