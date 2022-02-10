import smtplib
import os 

def send_email(message):

    sender_add= os.environ['sender_add']
    receiver_add= os.environ['receiver_add']
    password = os.environ['GMAIL']


    smtp_server=smtplib.SMTP("smtp.gmail.com",587)
    smtp_server.ehlo()

    smtp_server.starttls()
    smtp_server.ehlo()

    smtp_server.login(sender_add,password)

    msg_to_be_sent = str(message)
    

     
    smtp_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
    print('Successfully the mail is sent')

    smtp_server.quit()