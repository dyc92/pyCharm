#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'jiling5170 <jiling5170@163.com>'
receivers = ['gl308@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('''
    你好，在机器人技术和自动化中，控制环是一个控制系统状态的不终止的循环。
这是一个控制环的例子：房间里的温度自动调节器。
当你设置了温度，告诉了温度自动调节器你的期望状态。房间的实际温度是当前状态。通过对设备的开关控制，温度自动调节器让其当前状态接近期望状态。
控制器通过 apiserver 监控集群的公共状态，并致力于将当前状态转变为期望的状态
                   ''', 'plain', 'utf-8')
message['From'] = '<jiling5170@163.com>'   # 发送者
message['To'] = '<gl308@qq.com>'        # 接收者
message['Subject'] = Header('Header', 'utf-8')

try:
    smtpObj = smtplib.SMTP('smtp.163.com', 25)
    smtpObj.login('jiling5170@163.com', 'password')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as exc:
    print("Error: 无法发送邮件", exc)
