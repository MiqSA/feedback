# -- coding: utf-8 --
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar(destino, nome_cliente, end_email, senha):
    msg = MIMEMultipart()

    body = "Olá {}, tudo bem?".format(nome_cliente)
    msg.attach(MIMEText(body, 'plain'))
    html = """
       <html>
       <h3>Te peço um feedback!</h3>\
       </html>
       """
    msg.attach(MIMEText(html, 'html'))
    body = '\n'

    # Gmail Login
    fromaddr = end_email
    password = senha
    msg.attach(MIMEText(body, 'plain'))

    # Writing the message (this message will appear in the email)
    msg['Subject'] = 'Meu feebbak'

    # Specifying the from and to addresses
    toaddrs = [destino.lower()]
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddrs)

    # Sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()