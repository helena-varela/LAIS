import utilidades.matematica as matematica
import utilidades.saudacoes as saudacoes
import utilidades.relatorio as relatorio

# funções matemáticas
a = 6
b = 5

c = matematica.fatorial(a)
d = matematica.calcula_multiplicação(a,b)

print(c)
print(d)

# saudando usuário
saudacoes.bem_vindo("Helena")

# retorna o dobro
dobro = relatorio.relatorio_dobro(4)
print(dobro)