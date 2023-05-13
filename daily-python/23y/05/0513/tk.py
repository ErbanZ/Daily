'''
Date: 2023-05-13 20:04:49
LastEditors: r7000p
LastEditTime: 2023-05-13 20:06:33
FilePath: \daily-python\23y\05\0513\tk.py
'''

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label(frm, text="").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()