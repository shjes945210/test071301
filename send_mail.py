import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = "shjes945211@gmail.com"
receiver = ["applejack9972@gmail.com","shjes945212@gmail.com"]
for res in receiver :
    msg= MIMEMultipart()
    msg["From"] = sender
    msg["To"] = res
    header = Header("Test Send Email","utf-8")
    msg["Subject"] = header.encode()

    body = "This is email send from python"

    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"lwpd qjwp rewe zlaf") 
        server.sendmail(sender,res,msg.as_string())
    

print("success send email")