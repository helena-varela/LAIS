usuario = input("Qual seu nome? ").capitalize()
quantidade_livros = int(input("Quantos livros você já pegou emprestado? "))

if quantidade_livros == 0:
    print(f"Seja bem-vindo(a), {usuario}! Você ainda não pegou nenhum livro emprestado.")
elif quantidade_livros == 1:
    print(f"Seja bem-vindo(a), {usuario}! Você pegou apenas {quantidade_livros} livro emprestado.")
elif quantidade_livros < 0:
    print("Digite uma quantidade de livros válida.")
else:
    print(f"Seja bem-vindo(a), {usuario}! Você pegou {quantidade_livros} livros emprestados.")