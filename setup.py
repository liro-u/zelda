from cx_Freeze import setup, Executable

includefiles=[
    "audio",
    "graphics",
    "map",
    "code"
    ]
    
    

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="triforce.ico"
    )

setup(
    name="zelda",
    version="1.0",
    description="Une copie de zelda en moins bien",
    author="Noailles Valentin",
    options = {'build_exe' : {'include_files':includefiles}},
    executables=[target]
    )
