from functools import reduce

lista = [2, 3, 4]
produto = reduce(lambda x, y: x * y, lista)

print(produto)