import smtplib
from email.mime.text import MIMEText
_user =raw_input("user name")
_pwd  =raw_input("password")
_to   =raw_input("to")

msg = MIMEText("new episode")
msg["Subject"] = "new episode"
msg["From"]    = _user
msg["To"]      = _to


def send():
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException,e:
        print "Falied,%s"%e
