import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "andrescardenas280@gmail.com"
    # password = "pmumucgzwawvekau" # NOT SECURE
    password = os.getenv("PASSWORD") # Edit system environment variables

    receiver = "andrescardenas280@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        print("Email sent!")

if __name__ == '__main__':
    receiver = "andrescardenas280@gmail.com"

    message = """\
    Subject: Hi
    Hi!
    How are you?
    Bye!
    """

    send_email(message)