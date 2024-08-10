import tkinter as tk
import pyautogui
import threading
import keyboard

clicking = False

def update_label():
    label.config(text=f"현재 상태: {clicking} F5: 실행, F6: 중단")

def click(): 
    while clicking:
        pyautogui.sleep(0.01)
        pyautogui.click()

def start():
    global clicking
    clicking = True
    update_label()
    threading.Thread(target=click).start()

def stop():
    global clicking
    clicking = False
    update_label()

keyboard.add_hotkey('f5', start)
keyboard.add_hotkey('f6', stop)

root = tk.Tk()
root.title("AutoClick")

label = tk.Label(root, text=f"현재 상태: {clicking} F5: 실행, F6: 중단")
label.pack(pady=20)

root.mainloop()