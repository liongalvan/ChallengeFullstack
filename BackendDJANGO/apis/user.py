from apis.userData import Accounts


class user:
    name = str
    email = str
    document = str
    accounts = Accounts("", "", "", "")

    def __init__(self, name, email):
        self.name = name
        self.email = email
