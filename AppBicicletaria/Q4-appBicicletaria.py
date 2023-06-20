#---------------------------=---- Início das Variáveis Globais -------------------------------
listaPeca = []
codigoPeca = 0

#--------------------------------- Fim das Variáveis Globais ---------------------------------




#----------------------------- Início da Função cadastrarPeca() ------------------------------
def cadastrarPeca(codigo):
    print('Bem-vindo ao Menu de Cadastro de Peças')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Informe o NOME da peça: ')
    fabricante = input('Informe o FABRICANTE da peça: ')
    preco = int(input('Informe o PREÇO(R$) da peça: '))
    dicionarioPeca = {'codigo' : codigo, 'nome' : nome, 'fabricante' : fabricante, 'preco' : preco }
    listaPeca.append(dicionarioPeca.copy())
#----------------------------- Fim da Função cadastrarPeca() ---------------------------------



#---------------------------- Início da Função consultarPeca() -------------------------------
def consultarPeca():
    print('Bem-vindo ao Menu de Consulta de Peças')
    while True:
        opcaoConsulta = input('\nEscolha a opção desejada: \n' +
                               '1 - Consultar TODAS as Peças \n' +
                               '2 - Consultar Peças por CÓDIGO \n' +
                               '3 - Consultar Peças por FABRICANTE \n' +
                               '4 - Retornar \n' +
                               '>>')
        if opcaoConsulta == '1':
            print('Voce escolheu a opção Consultar TODAS as Peças')
            for peca in listaPeca: #peca vai varrer toda a lista de peças
                print('---------------------------------------')
                for key, value in peca.items():
                    print('{}: {}'.format(key,value)) #varer todos os conjuntos de chave e valor do dicionario peca
                print('---------------------------------------')

        elif opcaoConsulta == '2':
            print('Voce escolheu a opção Consultar Peças por CÓDIGO')
            valorDesejado = int(input('Informe o CÓDICO desejado: '))
            for peca in listaPeca:
                if peca ['codigo'] == valorDesejado: #o valor do campo codigo do dicionário é igual o valor desejado
                    print('---------------------------------------')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))  # varer todos os conjuntos de chave e valor do dicionario peca
                    print('---------------------------------------')

        elif opcaoConsulta == '3':
            print('Voce escolheu a opção Consultar Peças por FABRICANTE')
            valorDesejado = input('Informe o FABRICANTE desejado: ')
            for peca in listaPeca:
                if peca['fabricante'] == valorDesejado:  # o valor do campo fabricante do dicionário é igual o valor desejado
                    print('---------------------------------------')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))  # varer todos os conjuntos de chave e valor do dicionario peca
                    print('---------------------------------------')

        elif opcaoConsulta == '4':
            return  # sai da função consultarPeca e volta para o Main
        else:
            print('Opção Inválida! Tente Novamente')
            continue  # volta para o inicio do laço principal
#----------------------------- Fim da Função consultarPeca() ---------------------------------



#---------------------------- Início da Função removerPeca() ---------------------------------
def removerPeca():
    print('Bem-vindo ao Menu de Remoção de Peças')
    valorDesejado = int(input('Entre com o CÓDIGO que deseja remover: '))
    for peca in listaPeca:
         if peca['codigo'] == valorDesejado:
            listaPeca.remove(peca)
            print('Produto Removido')
#------------------------------- Fim da Função removerPeca() ---------------------------------



#-------------------------------------- Início do Main ---------------------------------------
print('Bem-vindo a Bicicletaria de Paula Alessandra Rodrigues dos Santos')
while True:
    opcaoPrincipal = input('\nEscolha a opção desejada: \n'+
                           '1 - Cadastrar Peças \n'+
                           '2 - Consultar Peças \n'+
                           '3 - Remover Peças \n'+
                           '4 - Sair \n'+
                           '>>')
    if opcaoPrincipal == '1':
        codigoPeca = codigoPeca + 1
        cadastrarPeca(codigoPeca)
    elif opcaoPrincipal == '2':
        consultarPeca()
    elif opcaoPrincipal == '3':
        removerPeca()
    elif opcaoPrincipal == '4':
        break #encera o laço principal e termina o programa
    else:
        print('Opção Inválida! Tente Novamente')
        continue #volta para o inicio do laço principal
#---------------------------------------- Fim do Main ----------------------------------------