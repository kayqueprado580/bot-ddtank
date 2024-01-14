# from cx_Freeze import setup, Executable


# executables = [Executable('seu_script.py')]


# setup(
#     name="pvp",
#     version="1.0",
#     description="pvp - bot",
#     executables=[Executable("pvp.py")],
#     options={
#         "build_exe": {
#             "include_files": 'img/',
#         },
#     },
# )

from cx_Freeze import setup, Executable

executables = [Executable('pvp.py')]

includes = ['pyautogui', 'time', 'cv2', 'logging', 'keyboard']

options = {
    'build_exe': {
        'includes': includes,
        'include_files': ['img/']
    }
}

setup(
    name='pvp-ddtank',
    version='1.0',
    description='bot',
    executables=executables,
    options=options
)