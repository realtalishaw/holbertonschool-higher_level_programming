#!/usr/bin/python3
#import smtp to send email + ss
import smtplib

#helper email module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#specify Email/pswd
email_user = "pythontestemail21@gmail.com"
email_password = "Est72093!"

#who the email is going to
email_send = ['misstalishawhite@gmail.com']

subject= 'Sending a lot of emails'

msg = MIMEMultipart()
msg['From'] = email_user

#converting list of recipients into comma separated string
msg['To'] = ", ".join(email_send)

msg['Subject'] = subject

body = 'Hello from the Otherside'
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()
