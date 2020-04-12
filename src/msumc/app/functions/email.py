import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(request, to_email, subject, message):
    from_email = request.registry.settings['from_email']
    from_passw = request.registry.settings['from_passw']

    s = smtplib.SMTP('smtp.gmail.com', 587)

    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    s.ehlo()
    s.starttls()
    s.login(from_email, from_passw)
    s.sendmail(from_email, to_email, msg.as_string())
    s.close()
