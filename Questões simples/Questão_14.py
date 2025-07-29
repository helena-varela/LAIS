def eh_primo(n):
    if n < 2:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True

n = int(input("Digite um número: "))

eh_primo(n)

if eh_primo(n):
    print("É primo")
else:
    print("Não é primo")