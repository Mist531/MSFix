import os
import keyboard
import tkinter as tk

def KillExplorer():
    print("kill explorer")
    os.system("taskkill /f /im explorer.exe")

def RestartExplorer():
    print("restart explorer")
    os.system("start explorer.exe")

def KillProgramm():
    print("kill programm")
    window.destroy()

window = tk.Tk()
window.geometry('250x100')
window.title("MS Fix")
lbl = tk.Label(window, text="ctrl+1 - kill explorer,\nctrl+2 restart explorer,\nctrl+3 - kill programm")
lbl.grid(column=0, row=0)

# Регистрируем обработчики клавиатуры в фоновом режиме
keyboard.add_hotkey('ctrl+1', KillExplorer)
keyboard.add_hotkey('ctrl+2', RestartExplorer)
keyboard.add_hotkey('ctrl+3', KillProgramm)

window.mainloop()
