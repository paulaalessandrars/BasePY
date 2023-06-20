#Inicio da função dimensoesObjeto()
def dimensoesObjeto():
    print('------------------------------------------ MENU 1 DE 3 - Dimensões Objeto -------------------------------------------')
    while True:
        try:
            alturaD = int(input('Informe a altura do objeto (cm):'))
            comprimentoD = int(input('Informe o comprimento do objeto (cm):'))
            larguraD = int(input('Informe a largura do objeto (cm):'))
            volumeD = alturaD * comprimentoD * larguraD
            if volumeD < 1000:
                return volumeD * 10
            elif volumeD >= 1000 and volumeD < 10000:
                return volumeD * 20
            elif volumeD >= 10000 and volumeD < 30000:
                return volumeD * 30
            elif volumeD >= 30000 and volumeD < 100000:
                return volumeD * 50
            else:
                print('Opção inválida! Volume maior que 100000(cm³) não é aceito')
        except ValueError: # Tratamento de erro, caso o usuário digite letras ou valores quebrados
            print('Opção inválida! Informe valores válidos!(dados numéricos e inteiros)')
            continue # Retorna para o início do laço
#Fim da função dimensoesObjeto()


#Inicio da função pesoObjeto()
def pesoObjeto():
    print('-------------------------------------------- MENU 2 DE 3 - Peso Objeto ----------------------------------------------')
    while True:
        try:
            pesoO = float(input('Informe o peso do objeto menor que 30 (kg):'))
            if pesoO < 0.1:
                return pesoO * 1
            elif pesoO >= 0.1 and pesoO < 1:
                return pesoO * 1.5
            elif pesoO >= 1 and pesoO < 10:
                return pesoO * 2
            elif pesoO >= 10 and pesoO < 30:
                return pesoO * 3
            else:
                print('Opção inválida! Peso maior que 30(kg) não é aceito')
        except ValueError: #Tratamento de erro, caso o usuário digite letras
            print('Opção inválida! Informe valores válidos!(apenas dados numéricos)')
            continue # Retorna para o início do laço
#Fim da função pesoObjeto()


#Inicio da função rotaObjeto()
def rotaObjeto():
    print('-------------------------------------------- MENU 3 DE 3 - Rota Objeto ----------------------------------------------')
    while True:
        rotaO = input('Informe a rota do objeto: \n'+
                      'RS - De Rio de Janeiro até São Paulo \n'+
                      'SR - De São Paulo até Rio de Janeiro \n'+
                      'BS - De Brasília até São Paulo \n'+
                      'SB - De São Paulo até Brasília \n'+
                      'BR - De Brasília até Rio de Janeiro \n'+
                      'RB - Rio de Janeiro até Brasília \n'+
                      '>>')
        rotaO = rotaO.upper() # Caso o usuario digite siglas com letra minúscula
        rotaO = rotaO.strip()  # Caso o usuario digite com espaço adicional
        if rotaO == 'RS' or rotaO == 'SR':
             return 1
        elif rotaO == 'BS' or rotaO == 'SB':
            return 1.2
        elif rotaO == 'BR' or rotaO == 'RB':
            return 1.5
        else:
            print('Opção inválida! Informe uma rota válida (RS/SR/BS/SB/BR/RB)')
            continue # Retorna para o inicio do laço
#Fim da função rotaObjeto()



#Inicio main
print('-------------------- Bem-vindo ao programa de Logística de Paula Alessandra Rodrigues dos Santos --------------------')
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensao * peso * rota
print('O valor total do pedido é de: R$ {:.2f} (Dimensão: R$ {:.2f}, Peso: R$ {:.2f}, Rota: R$ {:.2f})'.format(total,dimensao,peso,rota))