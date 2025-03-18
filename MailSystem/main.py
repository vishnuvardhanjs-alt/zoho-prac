from user import User
from mail import Mail

class Main:
    def __init__(self):
        self.users = {"hello@gmail.com" : User("vishnu", "hello@gmail.com","12345"), "hello2@gmail.com" : User("vishnu2", "hello2@gmail.com","12345")}
        self.emailIds = {"hello@gmail.com", "hello2@gmail.com"}
        self.usernames = {"vishnu", "vishnu2"}
        self.cur_user = None

    
    def authUser(self):
        email = input("Enter Email Address : ")
        password = input("Enter Password : ")

        if email in self.emailIds:
            if self.users[email].password == password:
                self.cur_user = email
                return True
            else:
                print("Password Wrong")
                return False
        else:
            print("User Not Found")
            return False

    def addUser(self):
        username = input("Enter Username : ")
        email = input("Enter Email Address : ")
        password = input("Enter Password : ")

        if username not in self.usernames and email not in self.emailIds:
            temp_user = User(username, email, password)
            self.users[email] = temp_user
            self.usernames.add(username)
            self.emailIds.add(email)
        else:
            print("Email or Username already Exist, please Try Again!...")
            self.addUser()
        

    def composeMail(self):

        if self.authUser():
            to_addr = input("Enter Reciever's Email : ")

            if to_addr not in self.emailIds:
                print("Invalid Receiver Email!")
                return
            
            subject = input("Mail Subject : ")
            content = input("Mail Content : ")

            cur_user = self.cur_user
            print(cur_user)
            temp_mail = Mail(cur_user, to_addr, subject, content)

            self.users[self.cur_user].addToSent(temp_mail)
            self.users[to_addr].addToInbox(temp_mail)
            self.cur_user = None



    def deleteMail(self):
        if self.authUser():
            self.users[self.cur_user].deleteMail()
            self.cur_user = None
        else:
            print("Password Wrong")
    
    def recallMail(self):
        if self.authUser():
            self.users[self.cur_user].recall(self.users)
            self.cur_user = None
        else:
            print("Password Wrong")

    def viewInbox(self):
        if self.authUser():
            self.users[self.cur_user].viewInbox()
            self.cur_user = None
        else:
            print("Password Wrong")
    
    def viewSent(self):
        if self.authUser():
            self.users[self.cur_user].viewSent()
            self.cur_user = None
        else:
            print("Password Wrong")


main = Main()

while True:
    print("1. Create User")
    print("2. Compose Mail")
    print("3. delete Mail")
    print("4. recall Mail")
    print("5. view inbox")
    print("6. view Sent Mail")
    print("7. Exit")

    opt = int(input("Enter the Option : "))

    if opt == 1:
        main.addUser()
    elif opt == 2:
        main.composeMail()
    elif opt == 3:
        main.deleteMail()
    elif opt == 4:
        main.recallMail()
    elif opt == 5:
        main.viewInbox()
    elif opt == 6:
        main.viewSent()
    elif opt == 7:
        print()
        break

    print()



