from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda val: val % 2 == 0, nums))

doubles = list(map(lambda val: val * 2, evens))

summary = reduce(lambda a, b: a + b , doubles)

print(evens, '\n', doubles, '\n', summary, sep='')
