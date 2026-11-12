class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(100)
account.balance = -1


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be posititve")
        else:
            self._balance += amount
            return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("I said that amount must be positive previous")
        if amount >= self._balance:
            raise ValueError("Not enough money")
        self._balance -= amount
        return self._balance


good_account = BankAccount()
print(good_account.deposit(100))
print(good_account.withdraw(99))

#Полиморфизм состоит в том чтобы предоставлять пользователю только функционал и скрывать внутреннюю логику!
#+ -  никакой логики внешне не нужно прописывать, методы для определенных проблем либо есть, либо нет!
