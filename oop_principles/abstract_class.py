from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def stop(self):
        print('stoping!')

class Laptop(Computer):
    def process(self):
        print('is running')

com = Laptop()       
com.process()
com.stop()


#ABC для определения класса как абстрактного и abstractmethod для определения какие методы нужно переназначить в подклассах!
#Абстрактные классы обычно используются для того чтобы создавать конкретные случаи - подклассы.
#+ - в полной мере раскрывается наследовательность и можно создать общий пример для какой-то области!