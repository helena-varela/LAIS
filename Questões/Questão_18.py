lista = [0, 25, 40]
transformar = lambda x: (x * 9/5) + 32
fahrenheit = list(map(transformar, lista))
print(fahrenheit)