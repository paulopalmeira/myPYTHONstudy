# Estrutura de Decisão  IF... ELIF.

nota1 = int (input("Digite a primeira nota:"))
nota2 = int (input("Digite a segunda nota:"))

print ("As notas digitadas foram: ", nota1, " ", nota2)

media = (nota1 + nota2) / 2

if (media>=6):
    print("Aluno aprovado")
elif (media>2):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")
