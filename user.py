

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
