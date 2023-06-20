# Início da função metragem_limpeza()

def metragem_limpeza():
    print('....................Menu 1 de 3 Metragem de Limpeza....................')
    while True:
        try:
            metragemL = int(input('Informe a metragem desejada (m²):'))
            if (metragemL >= 30) and (metragemL <= 300): # SE 30 <= metragem < 300, VALOR É 60 + 0.3 *  metragem.
                return metragemL * 0.3 +60
            elif (metragemL >= 300) and (metragemL <= 700):  # 300 <= metragem < 700, VALOR É 120 + 0.5 *  metragem.
                return metragemL * 0.5 + 120
            else:
                print('Opção inválida! Digite um valor igual ou acima de 30, ou igual ou abaixo de 700!!')
        except ValueError:
            print('Opção inválida!! Digite valores inteiros!!')
            continue #retorna para o começo do laço
# Fim da função metragem_limpeza()


# Início da função tipo_limpeza()
def tipo_limpeza():
    print('......................Menu 2 de 3 Tipo de Limpeza......................')
    while True:
        tipoL = input('Informe o tipo de limpeza desejado: \n'+
                      'B – Básica - Indicada para sujeiras semanais ou quinzenais \n'+
                      'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras '+
                      '>> ')
        tipoL = tipoL.upper()
        if tipoL == 'B':
            return 1.00  # SE B, O multiplicador é 1.00
        elif tipoL == 'C':
            return 1.30 # SE C, O multiplicador é 1.30
        else:
            print('Opção inválida! Informe uma opção válida (B/C):')
            continue #retorna para o começo do laço
# Fim da função tipo_limpeza()


# Início da função adicional_limpeza()
def adicional_limpeza():
    print('....................Menu 3 de 3 Adicional de Limpeza...................')
    acumulador = 0
    while True:
        adicionalL = input('Deseja algo mais? \n'+
                      '0 - Não desejo mais nada (encerrar) \n'+
                      '1 - Passar 10 peças de roupas - R$ 10.00 \n'+
                      '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                      '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                      '>> ')
        if adicionalL == '0':
             return acumulador
        elif adicionalL == '1':
             acumulador = acumulador + 10
             continue #volta para o incio do laço
        elif adicionalL == '2':
             acumulador = acumulador + 12
             continue  # volta para o incio do laço
        elif adicionalL == '3':
             acumulador = acumulador + 20
             continue  # volta para o incio do laço
        else:
            print('Opção inválida! Informe uma opção válida (0/1/2/3):')
# Fim da função adicional_limpeza()


#Inicio do Main():
print('Bem-vindo a Empresa de Limpeza de Paula Alessandra Rodrigues dos Santos!')
metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicional = adicional_limpeza()
total = (metragem * tipo) + adicional
print('O total a ser pago é: R$ {:.2f} (Metragem: R$ {:.2f}, Tipo: R$ {:.2f}, Adicional: R$ {:.2f})'.format(total, metragem, tipo, adicional))
