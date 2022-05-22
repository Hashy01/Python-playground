import tkinter as tk # Help us read GUI
from tkinter import filedialog, Text #filedialog used to select app #text dis
import os

#root is like HTML the body (keeps the whole structure) attach button etc to the root.
root = tk.Tk() 

canvas = tk.Canvas(root, height=700, width=700, bg = "#263D42")
canvas.pack()

root.mainloop()
