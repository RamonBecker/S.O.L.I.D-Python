

class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod
    def members():
        return ['username1', 'username2', 'team1']
