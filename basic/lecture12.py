import smtplib
from email.mime.text import MIMEText
# my_smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
# or my_smtp=smtplib.SMTP("smtp.gmail.com",587); my_smtp.starttls()
# my_smtp.login(id,pwd)
# my_smtp.sendmail(from,to,"data")
# my_smtp.quit()
# https://support.google.com/accounts/answer/185833

me="---@gmail.com"
you="---@gmail.com"

my_smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
my_smtp.login(me,"---")
msg=MIMEText("hi, test")
msg['Subject'] = 'Test Python'
my_smtp.sendmail(me,you,msg.as_string())
my_smtp.quit()
