dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# a linha abaixo vai retorar um erro pq não é possível alterar o valor de tupla
# dimensions[0] = 250

dimensions = (200,50)
print("Dimensões originais:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)

print("\nDimensões modificadas:")
for dimension in dimensions:
    print(dimension)


