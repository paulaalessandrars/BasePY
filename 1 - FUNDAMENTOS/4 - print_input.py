nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade ")

#print(nome)
#print(idade)

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")

print(f'Seu nome é {nome} e sua idade é {idade}')