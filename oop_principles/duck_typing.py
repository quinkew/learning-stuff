class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class Laptop:
    
    def code(self, ide):
        ide.execute()

ide = PyCharm()
ide1 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
lap1.code(ide1)

#утиная типизация позволяет абстрактно реализовать метод класса, то есть мы не зависим от какого одного класса