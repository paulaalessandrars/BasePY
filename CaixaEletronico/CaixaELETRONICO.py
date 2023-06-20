#Um caixa eletrônico tem disponível apenas notas de 5, 20 e 50 reais. Crie um algoritmo que recebe como entrada o valor que se deseja sacar e retorne a menor quantidade de notas que compõem esse valor.
#Ex1: para um saque de R$ 25, o algoritmo retornaria que são 2 notas, uma de 5 e uma de 20.
#Ex2: para um saque de R$ 175, o algoritmo retornaria que são 5 notas, três de 50, uma de 20 e uma de 5.

valor = int(input('Informe o valor que deseja retirar:'))

while True:

    if valor >= 50:
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        print('Cedulas de 50: {}'.format(cedulas50))
        if not valor:
            break

    if valor >= 20:
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        print('Cedulas de 20: {}'.format(cedulas20))
        if not valor:
            break

    if valor >= 5:
        cedulas5 = valor // 5
        valor -= cedulas5 * 5
        print('Cedulas de 5: {}'.format(cedulas5))
        if not valor:
            break

    if valor:
        cedulas1 = valor
        print('Cedulas de 1: {}'.format(cedulas1))
        break
