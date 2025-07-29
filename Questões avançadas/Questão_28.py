pacientes = []
print("Bem-vindo ao cadastro, digite sair para terminar o cadastro")
while True:
    nome = input("Nome do paciente: ")
    if nome == "sair":
        break
    else:
        idade = input("Idade do peciente: ")
        sintomas = input("Sintomas do paciente: ")
        paciente = {
            "nome": nome,
            "idade": idade,
            "sintomas": sintomas
        }
        
        pacientes.append(paciente)

print("Relatório dos pacientes: ")
for paciente in pacientes:
    print(f"Nome: {paciente['nome']} \nIdade: {paciente['idade']} \nSintomas: {paciente['sintomas']}")