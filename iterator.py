class TopTen:             #реализация итератора через класс

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            
            val = self.num
            self.num += 1
            
            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)

nums = [7, 8, 9, 5]       #реализация через встроенную функцию python
it = iter(nums)

#То есть итератор позволяет обрабатывать объект лениво, то есть по одному элементу в разных строках кода
#+ - экономит память потому что не нужно перебирать все сразу
