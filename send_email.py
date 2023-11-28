import smtplib
import ssl
from decouple import config

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = config("USERNAME")
    password = config("PASSWORD")
    receiver = config("USERNAME")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)