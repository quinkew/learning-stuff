#  @property and setter


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email


user1 = User("Danila", "porperty@mail.ru", "hashed_successfully")
user1.email = "lajflk@salkdjf"
print(user1.email)
