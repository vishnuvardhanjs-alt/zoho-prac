class Mail:
    def __init__(self, from_address, to_address, mail_subject, mail_content):
        self.from_address = from_address
        self.to_address = to_address
        self.subject = mail_subject
        self.content = mail_content
        self.status = 'Sent'

    def viewMail(self):
        print(self.content)