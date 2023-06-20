# Hora de programar um jogo! Seu código deve gerar um número aleatório dentro de um intervalo escolhido
# pelo próprio jogador, que servirá como resposta, e solicitar que o usuário tente adivinhá-lo.
# A partir da resposta do usuário:
# a. Se a tentativa do usuário for maior ou menor que a resposta,
# o jogo deve informar ao usuário e solicitar um novo chute.
# b. Se a resposta for correta, o jogo deve avisar ao usuário que
# ele acertou e informar o número de tentativas utilizadas.


from random import randint

def numero():
    return randint(1, 100)

def jogo():
    resposta = numero()
    tentativa = 0
    print("\nAdivinhe o Número!")

    chute = 0
    while chute is not resposta:
        tentativa += 1
        chute = int(input("Qual seu chute? "))
        if chute > resposta:
            print("Errou! É um valor menor.")
        elif chute < resposta:
            print("Errou! É um valor maior.")
        else:
            print("Parabéns! O número é",resposta,"."\
                  " Você acertou em",tentativa,"tentativas!")
while True:
    jogo()



