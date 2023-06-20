print('Bem-vindo a Loja de Paula Alessandra Rodrigues dos Santos!')

valor_produto = float(input('Entre com o valor do produto desejado:'))

qtd_produto = int(input('Entre com a quantidade desejada:'))

vlr_sfrete = valor_produto * qtd_produto # VALOR SEM FRETE #

vlr_cfrete = 0

# VALOR COM FRETE INCLUSO #


if qtd_produto < 11: # SE 0 <= quantidade < 11,  o valor do frete é 30 #
    vlr_cfrete = (valor_produto * qtd_produto) + 30

elif(qtd_produto >= 11) and (qtd_produto < 101): # SE NÃO E FOR 11 <= quantidade < 101, O VALOR DO FRETE É 60 #
    vlr_cfrete = (valor_produto * qtd_produto) + 60

elif(qtd_produto >= 101) and (qtd_produto < 1001): # SE NÃO E FOR 101 <= quantidade < 1001, O VALOR DO FRETE É 120 #
    vlr_cfrete = (valor_produto * qtd_produto) + 120

else: vlr_cfrete = (valor_produto * qtd_produto) + 240 # SE NÃO FOR NENHUMA DAS ANTERIORES ENTÃO A quantidade >= 1001, O VALOR DO FRETE É 240 #


print('O valor total sem frete é: {}'.format(vlr_sfrete))

print('O valor total com frete é: {}'.format(vlr_cfrete))




