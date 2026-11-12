# Static methods


class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount_of_money):
        if self._is_valid_amount(amount_of_money):
            self.balance += amount_of_money
            self.__log__transaction("deposit", amount_of_money)
        else:
            print("Deposit amount must be positive")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log__transaction(self, transactyon_type, amount):
        print(
            f"Logging {transactyon_type} of ${amount}. New balance is ${self.balance}"
        )

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Marin", 500)
account.deposit(100)
