import os
import subprocess as sp

paths = {
    'notepad': r"C:\windows\system32\notepad.exe",
    'discord': r"C:\Users\Vansh\AppData\Local\Discord\Update.exe",
    'calculator': r"C:\windows\system32\calc.exe"
}

def notepad():
    os.startfile(paths['notepad'])

def discord():
    os.startfile(paths['discord'])

def cmd():
    os.system('start cmd')

def camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def calculator():
    sp.Popen(paths['calculator'])
