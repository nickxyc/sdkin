#encoding=utf-8
import tkinter as tk
from find_file import *
from tkinter import messagebox
from sendmail import sendmail
from save_json import savejson
import sys
page = 0
submit_cofirm_num = 0
def dstroy_welcom_window():
    welcome_window.destroy()
def command_(var,basename):
    if var.get() == 1:
        if tk.messagebox.askyesno(message='是否将这个文件发送到你的kindle上'):
            sendmail(basename)
def page_down(file_list):
    global page
    page  = page + 3
    checkbutton(file_list)
def page_up(file_list):
    global page
    page = page -3
    checkbutton(file_list)
def submit_cofirm(ad,pw,kindle_email):
    if not ad[-6:] == 'qq.com':
        messagebox.showerror(message='请输入QQ邮箱')
        sys.exit()
    messagebox.showinfo(message='提交成功')
    savejson(ad,pw,kindle_email)
    dstroy_welcom_window()
def checkbutton(file_list):
    global page
    var1 = tk.Variable()
    var2 = tk.Variable()
    var3 = tk.Variable()
    varA = tk.IntVar()
    varB = tk.IntVar()
    varC = tk.IntVar()
    try:
        var1.set(file_list[page])
        c1 = tk.Checkbutton(window, textvariable=var1, variable=varA, onvalue=1, offvalue=0, command=lambda :command_(varA,var1.get()))
        c1.pack()
        c1.place(x =100,y = 75)
    except:
        tk.messagebox.showerror(message='没有了')
    try:
        var2.set(file_list[page+1])
        c2 = tk.Checkbutton(window,textvariable = var2,variable = varB,onvalue = 1,offvalue = 0,command = lambda :command_(varB,var2.get()))
        c2.pack()
        c2.place(x = 100,y = 100)
    except:
        pass
    try:
        var3.set(file_list[page+2])
        c3 = tk.Checkbutton(window, textvariable=var3, variable=varC, onvalue=1, offvalue=0,command=lambda: command_(varC,var3.get()))
        c3.pack()
        c3.place(x = 100,y = 125)
    except:
        pass
    if len(file_list)>page+3:
        b2 = tk.Button(window,text = 'next',command =lambda :page_down(file_list))
        b2.pack()
        b2.place(x = 250,y = 150)
    if page != 0:
        b3 = tk.Button(window,text = 'forward',command =lambda :page_up(file_list))
        b3.pack()
        b3.place(x= 0,y = 150)
def Buttonfunction(filelist):
    find_file()
    checkbutton(filelist)
welcome_window = tk.Tk()
welcome_window.title('login')
welcome_window.geometry('500x300')
email_address = tk.Entry(welcome_window)
email_address.pack()
email_address_pw = tk.Entry(welcome_window)
email_address_pw.pack()
kindle_email = tk.Entry(welcome_window)
kindle_email.pack()
exitbutton = tk.Button(welcome_window,text = '确认',command = lambda :submit_cofirm(email_address.get(),email_address_pw.get(),kindle_email.get()))
exitbutton.pack()
escapebutton = tk.Button(welcome_window,text = '跳过',command = dstroy_welcom_window).pack()
welcome_window.mainloop()
window = tk.Tk()
window.title('sendkindle')
window.geometry('300x200')
file_list = filelist()
l = tk.Label(window,text = '在需要发送的文件前面打勾即可',width = 20,height = 2)
l.pack()
l.place(x = 2,y = 2)
Buttonfunction(file_list)
window.mainloop()