from functools import reduce

print(reduce(lambda x, y: x * y, [n for n in range(100, 1001) if n % 2 == 0]))
