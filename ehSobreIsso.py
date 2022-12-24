# Em python, colchetes [] indicam uma lista

carros = ['gol', 'opala', 'bmw']

# Escrever o primeiro carro em letras maiúsculas

print(carros[0].upper())

# Escrever o segundo carro com a primeira letra maiúscula

print(carros[1].title())

# Adicionar um item à lista

carros. append('Mercedes')

print(carros)

carros.insert(4,'Ferrari')

print(carros)

# pra deletar 

del carros[1]

print(carros)

# usando o POP remove o último da lista

carros.pop()
print(carros)

# da pra usar o pop pra deletar qualquer item

carros.pop(0)
print(carros)


