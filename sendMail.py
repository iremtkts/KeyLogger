import smtplib
import time
import os.path

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendMails():
    while True:
        try:
            email = 'YOUR EMAIL'
            password = 'YOUR PASSWORD'
            send_to_email = 'YOUR EMAIL'
            subject = 'This is the subject'
            message = 'This is my message'
            file_location = 'C:\\pythonprojects\\projects\\lab_odev\\files.zip'

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            filename = os.path.basename(file_location)
            attachment = open(file_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()
        except:
            print(NameError)
        time.sleep(60*5)
