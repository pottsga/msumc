import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(request, to_email, subject, message):
    from_email = request.registry.settings['from_email']
    from_passw = request.registry.settings['from_passw']

    s = smtplib.SMTP('smtp.gmail.com', 587)

    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = FROM_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    s.starttls()
    s.login(from_email, from_passw)
    s.sendmail(FROM_EMAIL, to_email, msg.as_string())