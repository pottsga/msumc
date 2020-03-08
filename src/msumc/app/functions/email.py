import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

FROM_EMAIL = "msumc.system@gmail.com"
FROM_PASSW = "scraggly-pliable-banjo"

def send_email(to_email, subject, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = FROM_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    s.starttls()
    s.login(FROM_EMAIL, FROM_PASSW)
    s.sendmail(FROM_EMAIL, to_email, msg.as_string())
