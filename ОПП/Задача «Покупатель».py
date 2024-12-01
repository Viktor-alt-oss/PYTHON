class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Банк работает только с числами')
        
    def withdraw(self, value):
        if not Customer.check_type(value) and self.balance >= value:
            self.balance -= value
        else:
            raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        if not Customer.check_type(value):
            self.balance += value
        


