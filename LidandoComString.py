name='Maiusculas e Minusculas'
print(name.upper())
print(name.lower())

first_name="Paulo"
last_name="Palmeira"

full_name = first_name + " " + last_name
print(full_name)

# tabulação
print("\tPython")
print("\t\tPython")

# quebra de linha na string

print("Linguagens:\nPython\nC\nJavaScript")

# removendo espaços em branco no final da string - lado direito

txt = "    banana     "
y = txt.rstrip()
print(y + name)

# removendo caracteres da string
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

# usar inteiros em string

idade=40
message="Voce tem " + str(idade) + " anos de idade"
print(message)






