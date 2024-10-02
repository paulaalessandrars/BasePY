nome = "Paula"

print(nome.upper())

print(nome.lower())

print(nome.title())

texto = "  Olá mundo!  "


print(texto)

# strip para remover o espaço em branco
print(texto.strip())

print(texto.rstrip()) # rstrip para remover o espaço em branco da direita

print(texto.lstrip()) # lstrip para remover o espaço em branco da esquerda




menu = "Python"

# todos abaixo tem o mesmo proposito, mas o ultimo exemplo é o mais prático para utlizar no menu, pois nao precisamos ficar pensando ou fazendo conta para centralizar

print("####" + menu + "####")

print(menu.center(14))

print(menu.center(20, "#"))


# O join é para quando eu quiser que fique tracejado e não precisar fazer uma iteração para isso
print("P-y-t-h-o-n")

print("-".join(menu))



