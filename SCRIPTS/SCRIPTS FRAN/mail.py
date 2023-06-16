import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envio(dato):
    recoge = (dato['ahora'] - dato['antes']) * 100000000
    saldo = dato['ahora']*100000000
    print ( recoge)
    sender_email = "python.arb@gmail.com"
    receiver_email = "frjcastilla@gmail.com"
    password = "yjmaafpukcayacts"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Ronda Finalizada"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    He terminado"""
    html = """\
    <html>
      <body>
        <p>Hola,<br>
           he recogido  """+str(recoge) + """        </p>
        <p>Total = """+str(saldo)+"""</p>
      </body>
    </html>
     """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

