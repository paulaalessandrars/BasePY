print('Bem-vindo a Sorveteria de Paula Alessandra Rodrigues dos Santos!')

print('............................................CARDÁPIO.............................................')
print('| Código |       Descrição      | Tamanho P (500 ml) | Tamanho M (1000 ml) | Tamanho G(2000 ml) |')
print('|   TR   | Sabores Tradicionais |       R$ 6,00      |       R$ 10,00      |      R$ 18,00      |')
print('|   ES   |  Sabores Especiais   |       R$ 7,00      |       R$ 12,00      |      R$ 21,00      |')
print('|   PR   |   Sabores Premium    |       R$ 8,00      |       R$ 14,00      |      R$ 24,00      |')
print('.................................................................................................')

acumulador = 0

while True:
    tamanho = input('Entre com o tamanho do pote de sorvete desejado (P/M/G): ')
    tamanho = tamanho.upper() # Para resolver problema de digitação caso o usuário digite minúscula ou maiúscula.
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('OPÇÃO INVÁLIDA!! Informe um tamanho válido (P/M/G)')
        continue # Se o usuário digitar algo inválido volta para o inicio do while.

    codigo = input('Entre com o codigo do sorvete desejado (TR/ES/PR): ')
    codigo = codigo.upper() # Para resolver problema de digitação caso o usuário digite minúscula ou maiúscula.
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('OPÇÃO INVÁLIDA!! Informe um código válido (TR/ES/PR)')
        continue # Se o usuário digitar algo inválido volta para o inicio do while.


#SABORES TRADICIONAIS:
    if codigo == 'TR' and tamanho == 'P':
        print('Você escolheu: SABOR TRADICIONAL, TAMANHO P')
        acumulador = acumulador + 6 # pegar valor no acumulador e somar + 6.

    elif codigo == 'TR' and tamanho == 'M':
        print('Você escolheu: SABOR TRADICIONAL, TAMANHO M')
        acumulador = acumulador + 10 # pegar valor no acumulador e somar + 10.

    elif codigo == 'TR' and tamanho == 'G':
        print('Você escolheu: SABOR TRADICIONAL, TAMANHO G')
        acumulador = acumulador + 18 # pegar valor no acumulador e somar + 18.

# SABORES ESPECIAIS:
    elif codigo == 'ES' and tamanho == 'P':
        print('Você escolheu: SABOR ESPECIAL, TAMANHO P')
        acumulador = acumulador + 7 # pegar valor no acumulador e somar + 7.

    elif codigo == 'ES' and tamanho == 'M':
        print('Você escolheu: SABOR ESPECIAL, TAMANHO M')
        acumulador = acumulador + 12 # pegar valor no acumulador e somar + 12.

    elif codigo == 'ES' and tamanho == 'G':
        print('Você escolheu: SABOR ESPECIAL, TAMANHO G')
        acumulador = acumulador + 21  # pegar valor no acumulador e somar + 21.

#SABORES PREMIUM:
    elif codigo == 'PR' and tamanho == 'P':
        print('Você escolheu: SABOR PREMIUM, TAMANHO P')
        acumulador = acumulador + 8 # pegar valor no acumulador e somar + 8.

    elif codigo == 'PR' and tamanho == 'M':
        print('Você escolheu: SABOR PREMIUM, TAMANHO M')
        acumulador = acumulador + 14 # pegar valor no acumulador e somar + 14.

    elif codigo == 'PR' and tamanho == 'G':
        print('Você escolheu: SABOR PREMIUM, TAMANHO M')
        acumulador = acumulador + 24 # pegar valor no acumulador e somar + 24.

    mais_pedido = input('Deseja pedir mais algum sorvete (S/N)?:')
    mais_pedido = mais_pedido.upper() # Para resolver problema de digitação caso o usuário digite minúscula ou maiúscula.
    if mais_pedido == 'S':
        continue
    else:
        print('O valor a ser pago é: R$ {:.2f}'.format(acumulador))
        break











