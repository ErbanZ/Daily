'''
Date: 2023-05-13 20:04:49
LastEditors: r7000p
LastEditTime: 2023-05-15 23:22:28
FilePath: \daily-python\23y\05\0513\tk.py
'''

from tkinter import *
from tkinter import ttk

# 创建 Tk 对象实例，初始化 Tk 并创建与其关联的 Tcl 解释器
# 创建一个顶层窗口，名为 root 窗口，它将被作为应用程序的主窗口
root = Tk()

# 创建了一个框架控件，包含创建的一个标签和一个按钮
# 框架被嵌在 root 窗口内部
frm = ttk.Frame(root, padding=100)

# grid() 方法被用来指明标签在包含它的框架控件中的相对布局（定位）
# 作用类似于 HTML 中的表格
frm.grid()

# 标签控件，展示文本
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label(frm, text="").grid(column=0, row=1)

# 按钮控件
# 当按下时将调用 root 窗口的 destroy() 方法
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

# print(set(ttk.Button().configure().keys()) - set(ttk.Frame().configure().keys()))
print(set(ttk.Label().configure().keys()))
# print(set(dir(ttk.Button())) - set(dir(ttk.Frame())))

root.mainloop()

