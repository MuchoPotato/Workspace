import pyautogui
import time
import tkinter as tk

time.sleep (2)
print (pyautogui.position())

root = tk.Tk()
label = tk.Label(root, text=pyautogui.position())
label.pack()

root.mainloop()