

class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def pay_bill(self):
        raise NotImplementedError


    def code(self):
        raise NotImplementedError