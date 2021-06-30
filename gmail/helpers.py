from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def get_item_from_file(filename):
    with open(filename) as file:
        file_items = []
        line = file.readline()

        while line:
            file_items.append(line.strip())
            line = file.readline()
    return file_items


def get_email_msg(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list), "ERROR: 'send_to', is not a list"
    
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    if text != None:
        msg.attach(MIMEText(text))
    
    if files != [None]:
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        
    return msg.as_string()
