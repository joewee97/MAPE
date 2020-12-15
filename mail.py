from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#mailing notifications
smtp_username = "mape.notifications@gmail.com"
smtp_password = "Monitorp97"
#google SMTP server
smtp_host = "smtp.gmail.com"
smtp_port = 587 

#method to send email to user for low water storage
def sendUserMail():
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = "17100520@imail.sunway.edu.my" #insert email
    #may need to change to a changing variable for multiple users, subject, body
    msg['Subject'] = "Water Storage Notification"
    body = "Attention! Your water storage has ran out of water! Please fill it up as soon as possible. :'("
    msg.attach(MIMEText(body))
    #msg.attach(MIMEText(body, 'html'))
    print(msg)
    server = smtplib.SMTP(smtp_host,smtp_port)
    #587 = port that will be used by SMTP provider (Google)
    server.starttls()
    #login to mailing account
    server.login(msg['From'], smtp_password)
    #sends message to recipient
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    return
