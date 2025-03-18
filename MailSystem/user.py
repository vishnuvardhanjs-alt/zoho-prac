class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.inbox = []
        self.sent = []

    
    def addToInbox(self, mail):
        self.inbox.append(mail)

    def addToSent(self, mail):
        self.sent.append(mail)

    def recall(self, users):
        print(self.sent)
        for mail in range(len(self.sent)-1,-1,-1):
            print("Mail_id : ",mail+1 )
            print("To : ",self.sent[mail].to_address,"\n")
            print("Subject : ", self.sent[mail].subject)
            print()
        
        mail_id = int(input("Enter Mail ID : "))

        cur_mail = self.sent[mail_id-1]
        cur_mail.status = "Recalled"

        users[cur_mail.to_address].inbox.remove(cur_mail)

        
    def deleteMail(self):
        for mail in range(len(self.inbox)-1,-1,-1):
            print("Mail_id : ",mail+1 )
            print("From : ",self.inbox[mail].from_address,"\n")
            print("Subject : ", self.inbox[mail].subject)
            print()
        
        mail_id = input("Enter Mail ID : ")
        self.inbox.pop(mail_id-1)


    def viewInbox(self):
        for mail in range(len(self.inbox)-1,-1,-1):
            print("From : ",self.inbox[mail].from_address,"\n")
            print("Subject : ", self.inbox[mail].subject,"\n")
            print(self.inbox[mail].subject)
            print()

    def viewSent(self):
        for mail in range(len(self.sent)-1,-1,-1):
            print("Status : ", self.sent[mail].status)
            print("From : ",self.sent[mail].from_address)
            print("Subject : ", self.sent[mail].subject)
            print(self.sent[mail].subject)
            print()