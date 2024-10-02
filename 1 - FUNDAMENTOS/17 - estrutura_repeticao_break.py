# while True:
#     numero = int(input("Informe um número: "))

#     if numero == 10:
#         break

#     print(numero)


# for numero in range(100):

#     if numero == 11:
#         break # para a execução

#     print(numero, end=" ")



for numero in range(100):

    if numero % 2 == 0:
        continue # pula a execução

    print(numero, end=" ")


# Lê a entrada do usuário, que será um número inteiro
numero = int(input())

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")



# Lê a entrada do usuário, que será um número inteiro representando o ano
ano = int(input())

# Verifica se o ano é bissexto seguindo as regras
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("SIM")
else:
    print("NÃO")