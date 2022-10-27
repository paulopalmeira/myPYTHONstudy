print("Hello World")

# Números (inteiros, reais e complexos);
# String (cadeia de caracteres que representam um texto);
# Boolean;
# List;
# Tuple;
# Dicitonary

nome = "João da Silva"
idade = 25
email = "jose@gmail.com"
print (nome , idade , email)

#  Podemos atribuir valores em uma mesma linha a múltiplas variáveis. 
#  Para isso, basta digitar os valores separados por vírgula.

nome, idade, email = "Maria da Silva", 50, "maria@uol.com.br"
print (nome, idade, email)

# A sintaxe para a entrada de dados é: VARIÁVEL = INPUT ("MENSAGEM")

nome = input("Digite seu nome: ")
print("Olá, ", nome, ", tudo bem?")

#  Converte a entrada de dados para um tipo INT (Números Inteiros)

nome = input("Digite seu nome:")
idade = int (input("Digite sua idade:"))
peso = float (input("Digite seu peso:"))

print ("O nome digitado foi: ", nome)
print ("A idade informada foi: ", idade)
print ("O peso informado foi: ", peso)

# Para descobrir o tipo de uma variável ou objeto - Comando TYPE

lista = []
print( type(lista) )

dicionario = {}
print( type(dicionario) )

texto = 'a'
print( type(texto) )

numero = 23
print( type(numero) )

logico = False
print( type(logico) )

class Classe1 (object):
    pass

objeto = Classe1()
print( type(objeto) )

# Para TESTAR se uma variável ou objeto é de um determinado tipo, 
# deve utilizar o operador IS.

lista = []
print( type(lista) is list )

dicionario = {}
print( type(dicionario) is dict )

texto = 'a'
print( type(texto) is str )

numero = 23
print( type(numero) is int )

logico = False
print( type(logico) is bool )

class Classe1 (object):
    pass

objeto = Classe1()
print( type(objeto) is Classe1 )