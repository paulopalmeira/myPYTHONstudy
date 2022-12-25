idade=12
if idade < 4:
    preco = 0
elif idade < 18:
    preco = 3
elif idade < 65:
    preco = 10
elif idade >= 65:
    preco = 5

print("O preco eh: " + str(preco) + ".")

