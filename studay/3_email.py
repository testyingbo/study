#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 163、QQ邮箱发送邮件
# ----------1.跟发件相关的参数------
smtpserver = "smtp.163.com"            # 发件服务器
port = 465                                            # 端口
sender = "jia18211143643@163.com"                # 账号
psw = "test123"                         # 密码
receiver = "jia18211143643@126.com"        # 接收人


# ----------2.编辑邮件的内容------
subject = "这个是主题163"
body = '<p>这个是发送的163邮件</p>'  # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "jia18211143643@126.com"
msg['subject'] = subject
# ----------2.编辑邮件的内容------
# 读文件
# file_path = "result.html"
# with open(file_path, "rb") as fp:
#     mail_body = fp.read()
#
# msg = MIMEMultipart()
# msg["from"] = sender                       # 发件人
# msg["to"] = ";".join(receiver)             # 多个收件人list转str
# msg["subject"] = "这个我的主题999"              # 主题

# 正文
# body = MIMEText(body, "html", "utf-8")
# msg.attach(body)

# # 附件
# att = MIMEText(body, "base64", "utf-8")
# att["Content-Type"] = "application/octet-stream"
# att["Content-Disposition"] = 'attachment; filename="test_report.html"'
# msg.attach(att)

# ----------3.发送邮件------
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.connect(smtpserver)                      # 连服务器
smtp.login(sender, psw)                     # 登录
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()                                       # 关闭

