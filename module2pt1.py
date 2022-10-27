

# Estrutura de Decisão  IF ... ; IF ... ELSE ; e IF... ELIF.

a = 3
b = 4
soma = a + b
if (soma>6):
    print("Aluno aprovado")

# Entrada de dados e decisão

nota_A =  int( input ("Digite uma nota: "))
nota_B =  int( input ("Digite outra nota: "))

print ("As notas digitadas foram: ", nota_A , " ", nota_B)

media = (nota_A + nota_B) / 2

if (media>6):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")