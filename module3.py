# Estrutura de repetição FOR são excelentes quando temos um número predefinido de repetições.
# Vejamos uma sintaxe: 

# for <<variável>> in <<faixa de valores>>:

soma=0
for i in (0,1,2,3,4):
    soma=soma+3
    print(soma)

print(" - ")

for i in (5,10,55,115,210):
    print(i)


print(" - ")

# Para uma sequência finita, é utilizado em Python a função RANGE, uma função que
# gera uma sequência numérica. A sintaxe dessa função é:

# FOR X IN RANGE (X,Y,Z):
#   X é onde começa. Se omitido, começa no zero
#   Y é o número mais alto (não inclusivo) da sequência
#   Z é um incremento. Se omitido, valor é 1

for i in range (5):
    print(i)

print("")

for i in range(0,15,2):
    print(i)

print("")

# Escrever de 0 a 10 em ordem decrescente. Vamos ver:
# (10,  ,  ) -> começa com o 10
# (  ,-1,  ) -> o -1 é porque termina no zero (-1 na inclusivo)
# (  ,  ,-1) -> o -1 é porque conta menos um por vez


for i in range(10,-1,-1):
    print(i)

print("")

# Identificando quais números da sequência são múltiplos de 3.

qtdMultiplos=0
for i in range (1,30):
    if (i%3==0):
        qtdMultiplos+=1
        print(i)

print("A quantidade de números divisíveis por 3 na sequência de 1 a 30 é: ", qtdMultiplos)

# Linha 52: a cada repetição, essa linha é executada, e dessa forma, é testada a
# condição. Se o número atual da sequência (contido na variável “i”) dividido por três,
# resultar seu resto (por isso o operador de módulo) em zero, o número é divisível por
# 3 e assim, as linhas 4 e 5 serão executadas;
# da hora ;)

minhaString="ABCDEFGH"
for x in minhaString:
    print(x)


# Parei na página 15 da apostila 3... continuar daqui
