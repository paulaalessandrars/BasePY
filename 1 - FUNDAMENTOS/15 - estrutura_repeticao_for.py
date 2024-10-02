# Faz sentido usar for só quando eu sei o número de vezes que vai acontecer a repetição


# # texto = input("Informe um texto: ")
# texto = ""
# VOGAIS = "AEIOU"


# # Exemplo utilizando um iterável:

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="") # O end faz os numeros ficarem um do lado do outro.
# else:
#     print() # adiciona uma quebra de linha
#     print("Executa no final do laço")



# Exemplo utilizando a função built-in range

for numero in range(0, 51, 5): # o primeiro numero 0 é o inicio, o segundo numero 51 é onde eu quero que pare, e o terceiro numero 5 é o passo, que no caso é para contar de 5 em cinco. É a tabuada do 5.
    print(numero, end=" ")






def conta_vogais(s):
    # Define o conjunto de vogais, incluindo letras maiúsculas e minúsculas
    vogais = set('aeiouAEIOU')
    
    # Inicializa o contador de vogais
    contador = 0
    
    # Itera por cada caractere da string
    for char in s:
        # Verifica se o caractere é uma vogal
        if char in vogais:
            contador += 1
    
    # Retorna o número total de vogais
    return contador

# Exemplo de uso
entrada = input()
resultado = conta_vogais(entrada)
print(f"O número de vogais na string '{entrada}' é: {resultado}")
