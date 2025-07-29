import random

def jogar_dado():
    lista = []
    for i in range(3):
        numero = random.randint(1, 6)
        lista.append(numero)
    soma = sum(lista)
    return print(soma)