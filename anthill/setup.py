from cx_Freeze import setup, Executable

# Lista de scripts que você deseja incluir no executável
scripts = ["anthill.py"]

packages = ["numpy", "PIL"],

# Lista de módulos que você deseja incluir
includes = ["pyautogui", "time", "cv2", "logging", "keyboard", "ctypes"]

# Lista de imagens que você deseja incluir
include_files = [("img", "img"), ("log", "log"), ("pandora", "pandora")]

# Configurações para o executável
options = {
    "build_exe": {
        "packages": packages
        "includes": includes,
        "include_files": include_files,
    }
}

setup(
    name="anthill",
    version="1.0",
    description="bot - anthill - ddtank",
    executables=[Executable(script) for script in scripts],
    options=options,
)
