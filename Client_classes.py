class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return 'Клиент {}. Баланс: {}'.format(self.name, self.balance)
