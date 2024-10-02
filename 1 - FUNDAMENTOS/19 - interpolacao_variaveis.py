nome = "Paula"
idade = 30
profissão = "Programadora"
linguagem = "Python"
saldo = 45.435


dados = {"nome": "Paula", "idade": 30, "saldo": 45.435}

# old style
print("Nome: %s Idade %d" % (nome, idade))


# .format
print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {name} Idade: {age}".format(name=nome, age=idade))

print("Nome: {nome} Idade: {idade}". format(**dados))


# fstring:
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")