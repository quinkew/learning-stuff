f = open(r'file.txt', 'r')          #для текстового формата
# print(f.readline())
# print(f.readlines())

f1 = open('MyText', 'w')
# f1.write('something ')
# f1.write('people')

f2 = open('MyText', 'a')
# f2.write('\n some new words!')

for data in f:
    f1.write(data)


f = open('photo.jpg', 'rb')         #для бинарного формата, в том числе и для картинок

f1 = open('MyPhoto.jpg', 'wb')

for i in f:
    f1.write(i)
