import smtplib, ssl


def send_email(message):
    sender = "datascienceandaienegneer@gmail.com"
    password = 'ecri eafn hsxa wgqy'

    receiver = "gobackenddevelopment@gmail.com"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

