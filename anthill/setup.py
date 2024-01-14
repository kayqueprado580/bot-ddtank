from cx_Freeze import setup, Executable

scripts = ["anthill.py"]
packages = ["numpy", "PIL"]
includes = ["pyautogui", "time", "cv2", "logging", "keyboard", "ctypes"]
include_files = [
    ("img", "img"),
    ("pandora/img", "pandora/img"),
    ("log", "log"),
    ("pandora/log", "pandora/log"),
    ("pandora", "pandora"),
]

options = {
    "build_exe": {
        "packages": packages,
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
