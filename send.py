import smtplib
from email.mime.text import MIMEText
_user =
_pwd  =
_to   = 

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
