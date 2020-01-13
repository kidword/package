# -*- coding: utf-8 -*-
from MyQR import myqr
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os


# 背景图片浏览功能
def browse_picture():
    fileName = tkinter.filedialog.askopenfilename()
    fileName_picture.set(fileName)


# 保存路径浏览功能
def browse_save():
    fileName = tkinter.filedialog.asksaveasfilename()
    (filepath, name) = os.path.split(fileName)
    fileName_save.set(filepath)
    global tempfilename
    tempfilename += name


# 生成功能
def generate():
    content = e1.get()
    background = e2.get()
    save_location = e3.get()
    try:
        if background == '':
            myqr.run(words=content, save_dir=save_location, save_name=tempfilename, colorized=True)
        else:
            myqr.run(words=content, save_dir=save_location, picture=background, save_name=tempfilename, colorized=True)
            tkinter.messagebox.showinfo('提示', '成功')
    except ValueError as reason:
        tkinter.messagebox.showerror(title='错误', message=reason)
        tkinter.messagebox.showinfo('提示', '失败')


root = Tk()
root.title('制作个性二维码')  # 标题
root.resizable(0, 0)  # 不可调整大小
tempfilename = ''

# 文本部分
Label(root, text="链接内容：").grid(row=0, padx=5)
Label(root, text="图片背景：").grid(row=1, pady=10)
Label(root, text="保存路径：").grid(row=2, padx=5)

# 输入框部分
fileName_picture = StringVar()
fileName_save = StringVar()
e1 = Entry(root, width=40)
e2 = Entry(root, width=40, textvariable=fileName_picture)
e3 = Entry(root, width=40, textvariable=fileName_save)
e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)

# 按钮部分
b1 = Button(root, text='生成', bd=5, width=5, command=generate).grid(row=4, column=0, sticky=W, padx=10, pady=5)
b2 = Button(root, text='退出', bd=5, width=5, command=root.quit).grid(row=4, column=1, sticky=E, padx=10, pady=5)
b3 = Button(root, text='浏览', bd=2, width=5, command=browse_picture).grid(row=1, column=1, sticky=E)
b4 = Button(root, text='浏览', bd=2, width=5, command=browse_save).grid(row=2, column=1, sticky=E)

root.mainloop()
