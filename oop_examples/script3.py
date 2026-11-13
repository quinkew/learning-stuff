# Static attributes


class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username {self.username}| Email {self.email}")


user1 = User("Nik", "bigmember@gmail.com")
user2 = User("Joe", "middlemember@gmail.com")
user3 = User("Bobby", "smallmember@gmail.com")
