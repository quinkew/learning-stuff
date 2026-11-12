# Protected and private

from datetime import datetime


class User:
    def __init__(self, name, email, age=0):
        self.name = name
        self.__email = email
        self.age = age

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email


user1 = User("Antonio", "EXample@gmail.com", 27)
user2 = User("Frank", "franklyspeaking@gmail.com", 32)

print(user1.get_email())

user2.set_email("newemail.com")

print(user2.get_email())
