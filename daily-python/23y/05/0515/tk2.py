'''
Date: 2023-05-15 21:10:51
LastEditors: r7000p
LastEditTime: 2023-05-15 23:24:20
FilePath: \daily-python\23y\05\0515\tk2.py
'''
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.output = tk.Label()
        self.output.pack()
        self.entrythingy.pack()
        self.output["text"] = "0"


        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        self.output["text"] = "self.contents"
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()