from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
"""A module for Bhulkee automated script in form of OOP"""


class BulkMailer():
    """A class that handles the sending of emails"""
    
    #SOME IMPORTANT VARIABLES#
    SERVER = 'smtp.gmail.com'
    FROM = 'gabrielnworah6@gmail.com'
    PASS = ''
    

    def __init__(self):
        """A constructor for the Bulkmailer class"""

        self.heading = ""
        self.body = ""
        self.email_list = []

    def AppendMailAddress(self, maillist):
        """A method that appends emails in the mailist to the mail_list attribute"""
        
        if maillist == None:
            return None
        for mail in maillist:
            self.email_list.append(maillist)
        return

    def compose(self):
        """A method that composes the email heading and body"""

        msg = MIMEMultipart()
        msg['Subject'] = self.heading
        msg['From'] = self.FROM
        msg.attach(MIMEText(self.body))
        return msg
    
    def initializeAndSend(self):
        """A method to initialize the mail server and sends the email to the reciepient"""
        
        message = self.compose()
        try:
            server = smtplib.SMTP_SSL(self.SERVER)
        except Exception:
            return None
        server.set_debuglevel(0)
        server.ehlo()
        server.login(self.FROM, self.PASS)
        if self.email_list != None:
            for mail_address in self.email_list:
                server.sendmail(self.FROM, mail_address, message.as_string())
        else:
            return False
        server.quit()
        return True


# mail = BulkMailer()
# mail.heading = "Welcome to Bhulkee"
# mail.body = "Just testing my authomated script to see if it works!"
# mail.compose()
# mail.email_list.append('bhulkee1@gmail.com')
# mail.email_list.append('gabrielnworah6@gmail.com')
# mail.initializeAndSend()