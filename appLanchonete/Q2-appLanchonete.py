print('Bem-vindo a Lanchonete de Paula Alessandra Rodrigues dos Santos!')

print('...........................CARDÁPIO..........................')
print('|  Código |         Descrição         |      Preço (R$)     |')
print('|   100   |      Cachorro-Quente      |       R$ 9,00       |')
print('|   101   |   Cachorro-Quente Duplo   |       R$ 11,00      |')
print('|   102   |           X-Egg           |       R$ 12,00      |')
print('|   103   |         X-Salada          |       R$ 13,00      |')
print('|   104   |          X-Bacon          |       R$ 14,00      |')
print('|   105   |          X-Tudo           |       R$ 17,00      |')
print('|   200   |     Refrigerante Lata     |       R$ 5,00       |')
print('|   201   |        Chá Gelado         |       R$ 4,00       |')
print('.............................................................')


acumulador = 0

while True:
    codigo = input('Informe o produto desejado: ')
    codigo = codigo.upper() # Para resolver problema de digitação caso o usuário digite minúscula ou maiúscula.
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('OPÇÃO INVÁLIDA!! Informe um código válido (100/101/102/103/104/105/200/201)')
        continue # Se o usuário digitar algo inválido volta para o inicio do while.

#LANCHES:
    if codigo == '100':
        print('Você escolheu: Cachorro-Quente')
        acumulador = acumulador + 9 # pegar valor no acumulador e somar + 9.

    elif codigo == '101':
        print('Você escolheu: Cachorro-Quente Duplo')
        acumulador = acumulador + 11 # pegar valor no acumulador e somar + 11.

    elif codigo == '102':
        print('Você escolheu: X-Egg')
        acumulador = acumulador + 12 # pegar valor no acumulador e somar + 12.

    elif codigo == '103':
        print('Você escolheu: X-Salada')
        acumulador = acumulador + 13 # pegar valor no acumulador e somar + 13.

    elif codigo == '104':
        print('Você escolheu: X-Bacon ')
        acumulador = acumulador + 14 # pegar valor no acumulador e somar + 14.

    elif codigo == '105':
        print('Você escolheu: X-Tudo')
        acumulador = acumulador + 17 # pegar valor no acumulador e somar + 17.

    elif codigo == '200':
        print('Você escolheu: Refrigerante Lata')
        acumulador = acumulador + 5 # pegar valor no acumulador e somar + 5.

    elif codigo == '201':
        print('Você escolheu: Chá Gelado')
        acumulador = acumulador + 4 # pegar valor no acumulador e somar + 4.


    mais_pedido = input('Deseja pedir mais algum produto (S/N)?:')
    mais_pedido = mais_pedido.upper() # Para resolver problema de digitação caso o usuário digite minúscula ou maiúscula.
    if mais_pedido == 'N':
        print('O valor a ser pago é: R$ {:.2f}'.format(acumulador))
        break
    else:
        continue











