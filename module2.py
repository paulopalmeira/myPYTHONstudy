# Vai mostrar o valor das duas variáveis, separadas pelo que tiver entre aspas

A = 2
B = 5
print(A, B, sep="-")

# Ordem de prioridade (precedência entre operadores):
# Da esquerda para a direita, primeiro os parênteses.

a = 10
b = 20
c = 15
d = 5
e = (a + b) * c / d
print(e)

# Operadores relacionais

# == (Igualdade) Verifica se os valores de dois operandos são iguais ou não, se a resposta for SIM, a condição torna-se verdadeira (TRUE).

a = 20
b = 20

if(a==b):
    print("a é igual a b")


# != (Diferente) Verifica se os valores de dois operandos são iguais ou não, se a resposta for NÃO, a condição torna-se verdadeira (TRUE)

a = 10
b = 20

if(a!=b):
    print("a não é igual a b")


# > (maior que) < (menor que) >= (maior igual) <= (menor igual)

a = 20
b = 10

if(a>b):
    print("a é MAIOR que b")

a = 5
b = 10

if(a<b): 
    print("a é MENOR que b")

a = 30
b = 30

if(a>=b): 
    print("a é MAIOR OU IGUAL que b")

a = 40
b = 40

if(a<=b): 
    print("a é MENOR OU IGUAL que b")


# Operadores lógicos ( AND , OR, NOT )

# AND - Retorna verdadeiro se ambas as expressões resultarem como verdadeira.
# Todas as expressões são avaliadas antes que o operador AND seja aplicado.

a = 10
b = 10
c = 15
d = 5

if(a>=b) and (c>d): 
    print("a é maior ou igual que b e c é maior que d")


# OR - Retorna verdadeiro se pelo menos uma das expressões resultarem como verdadeira. 
# Caso a primeira expressão retorne como verdadeiro, o restante das expressões não é avaliado.

a = 10
b = 10
c = 5
d = 15

if(a>=b) or (c>d): 
    print("a é maior ou igual que b OU c é maior que d")

# NOT
# Retorna verdadeiro se a expressão à direita for avaliada como falsa. 
# Retorna falso se a expressão à direita for verdadeiro.

a = 5
b = 10

if not (a>b):
    print("a é MAIOR que b")
