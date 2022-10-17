class Accounts:
    name = str
    number = int
    currency = str
    balance = float

    def __init__(self, name, number, currency, balance):
        self.name = name
        self.number = number
        self.currency = currency
        self.balance = balance
