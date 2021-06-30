import os
from .Gmail import Gmail
from .helpers import get_item_from_file, get_email_msg

def main():
    msg = os.getenv('MESSAGE')
    if msg != None:
        with open(msg, "r") as filename:
            text = filename.read()
    else:
        text = None

    send_to = get_item_from_file(os.getenv('RECIPIENT'))
    send_from = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    subject = os.getenv('SUBJECT')
    attachment = [os.getenv('ATTACHMENT')]
    msg = get_email_msg(send_from, send_to, subject, text, attachment)
    gmail = Gmail(send_from, password)

    with gmail:
        gmail.server.sendmail(send_from, send_to, msg)
