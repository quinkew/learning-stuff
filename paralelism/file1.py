import time
import os

def clock():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0) % 5 == 0:
            yield '5 sec'
        else:
            input()
            yield 0

def query():
    for i in os.walk('C:\\'):
        yield i[0]
        

def main():
    date = query()
    alarm = clock()
    while True:
        d = next(date)
        a = next(alarm)
        print(d)
        if a: print(a)
        d = next(date)
        print(d)
        time.sleep(1)

main()