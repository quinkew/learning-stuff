from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda val: val % 2 == 0, nums))  #нужен чтобы выбрать у объекта элементы удовлетворяющие функции и создать новый объект

doubles = list(map(lambda val: val * 2, evens))       #нужен чтобы преобразовать каждый элемент объекта по функции и создать новый объект

summary = reduce(lambda a, b: a + b , doubles)        #нужен чтобы собрать из объекта все элементы и по функции сделать одно значение 

print(evens, '\n', doubles, '\n', summary, sep='')
