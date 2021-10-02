from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def pay_bill(self):
        return "Paying bills..."

    def code(self):
        pass
