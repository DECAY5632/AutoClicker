import tkinter as tk
import pyautogui
import threading
import keyboard

clicking = False

def click(): 
    while clicking:
        pyautogui.sleep(0.01)
        pyautogui.click()

def start():
    global clicking
    clicking = True
    threading.Thread(target=click).start()

def stop():
    global clicking
    clicking = False

keyboard.add_hotkey('f5', start)
keyboard.add_hotkey('f6', stop)

root = tk.Tk()
root.title("AutoClick")

label = tk.Label(root, text="F5: 실행, F6: 중단")
label.pack(pady=20)

root.mainloop()