# Basics


class Dog:
    def __init__(self, name="", breed="", owner=""):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof, whoof")


class Owner:
    def __init__(self, name, address, contract_number):
        self.name = name
        self.address = address
        self.phone_number = contract_number


owner1 = Owner("Owl", "Nekrasov", "7988365")
dog = Dog("Timur", "Style", owner1)

print(dog.owner.phone_number)
