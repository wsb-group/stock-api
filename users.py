

from user import User as usr

class Users:

    # def __init__(self, user):
    #     self.userList = dict()
    #     email = user.getEmail()
    #     print("email is: " + email)
    #     self.userList[email] =user

    def __init__(self):
        self.userList = dict()

    def getUser(self, email):
        return self.userList.get(email)

    def deleteUser(self, email):
         del self.userList[email]

    def addUser(self, user):
        self.userList[user.getEmail()] = user

    def getUsers(self):
        return self.userList

/