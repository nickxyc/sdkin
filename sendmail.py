import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.encoders import encode_base64
from email.utils import formataddr,parseaddr
from email.header import Header
from email.mime.base import MIMEBase
import smtplib
from save_json import loadjson
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def sendmail(basename):
    from_addr,pw,to = loadjson()
    #from_addr = '1104254583@qq.com'
    #to = 'nick_xyc@kindle.cn'
    smtp_server = 'smtp.qq.com'
    msg = MIMEMultipart()
    msg.attach(MIMEText('由自动发送程序发送到kindle上的图书','plain','utf-8'))
    msg['From'] = _format_addr('molika<1104254583@qq.com>')
    msg['Subject'] = Header('Convert')
    with open('D:\\sendkindle\\'+basename,'rb') as f :
        mime = MIMEBase('file','mobi',filename = basename)
        mime.add_header('Content-Disposition', 'attachment', filename= ('gbk','', basename))
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        mime.set_payload(f.read())
        encode_base64(mime)
        msg.attach(mime)
    try:
        server = smtplib.SMTP_SSL(smtp_server,465)
        server.set_debuglevel(0)
        server.login(from_addr,pw)
        server.sendmail(from_addr,[to],msg.as_string())
        tk.messagebox.showinfo(message='发送成功')
    except:
        tk.messagebox.showinfo(message='发送失败，请重试')
    finally:
        server.quit()