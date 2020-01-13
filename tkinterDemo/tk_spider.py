# -*- coding: utf-8 -*-

from test.config import DOWNLOAD
from test.t2 import MeiTuSpider

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.title('图片下载')
root.resizable(0, 0)


# 图片存储地址
def browse_picture():
    path_ = askdirectory()
    fileName_picture.set(path_)


def generate():
    # 执行下载
    get_select_value = number.get()
    path = str(fileName_picture.get()) + '/'
    if len(path) >= 2:
        addr_num.set('开始下载....')
        addr_num.get()
        style = get_select_value
        index_url = str(DOWNLOAD[style])
        download = MeiTuSpider(index_url)
        download.run(index_url, path=path)
    else:
        tkinter.messagebox.showerror(title='error', message='选择存储路径')


# 选择框部分
number = tk.StringVar()
cmb = ttk.Combobox(root, textvariable=number, width=40)
cmb.grid(row=0, column=1, sticky=tk.E)
cmb['value'] = ('女神', '极品', '嫩模', '网络红人', '风俗娘', '气质', '尤物', '爆乳', '性感',
                '诱惑', '美胸', '少妇', '长腿', '萌妹子', '萝莉', '可爱', '户外', '比基尼', '清纯', '唯美', '清新')
cmb.current(0)

# 文本部分
ttk.Label(root, text="请选择:").grid(column=0, row=0)
tk.Label(root, text="保存路径：").grid(row=1, pady=10)
tk.Label(root, text="下载说明：").grid(row=2, padx=5)

# 输入框部分

fileName_picture = tk.StringVar()
e2 = tk.Entry(root, width=40, textvariable=fileName_picture)
e2.grid(row=1, column=1, padx=0, pady=5, sticky=tk.W)
addr_num = tk.StringVar()
addr_num.set('选择存储路径后，点击下载按钮开始下载')
ft1 = tkFont.Font(size=10)
tk.Label(root, textvariable=addr_num, fg='#2080ff', font=ft1).grid(column=1, row=2, sticky=tk.W, padx=10)

# 设置窗口部分
root.iconbitmap('login.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 390
height = 150

# 三个按钮
tk.Button(root, text='下载', bd=5, width=5, command=generate).grid(row=4, column=0, sticky=tk.W, padx=10,
                                                                 pady=5)
tk.Button(root, text='退出', bd=5, width=5, command=root.quit).grid(row=4, column=1, sticky=tk.E, padx=10,
                                                                  pady=5)
tk.Button(root, text='浏览', bd=2, width=4, command=browse_picture).grid(row=1, column=1, sticky=tk.E)
root.geometry('%dx%d+%d+%d' % (width, height, (screen_width - width) / 2, (screen_height - height) / 2))

root.mainloop()

