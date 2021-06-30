import smtplib

class Gmail:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __enter__(self):
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()
            self.server.login(self.username , self.password)
        except:
            print('ERROR: Something went wrong during login process')
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.server.close()
