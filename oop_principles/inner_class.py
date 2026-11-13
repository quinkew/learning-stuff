class Student:

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollnumber)

st = Student('Navin', 2)
st2 = Student('Jenny', 3)

st.show()

# создать Inner class можно либо с помощью lap1 = st.lap, либо с помощью lap1 = Student.Laptop()


st.lap.show()