print ('Bem-vindo a Loja de Descontos de Paula Alessandra Rodrigues dos Santos!')
valorProduto = float(input('Entre com o valor do produto desejado:'))
qtdPorduto = int(input('Entre com a quantidade desejada:'))
totalSemDesconto = valorProduto * qtdPorduto
totalComDesconto = 0

if qtdPorduto < 10: # Condição sem desconto
    totalComDesconto = totalSemDesconto # Não houve desconto aqui

elif qtdPorduto >= 10 and qtdPorduto < 100: # Condição com desconto de 5%
    totalComDesconto = totalSemDesconto - totalSemDesconto*(0.05) # Houve desconto de 5% aqui

elif qtdPorduto >= 100 and qtdPorduto < 1000: # Condição com desconto de 10%
    totalComDesconto = totalSemDesconto - totalSemDesconto*(0.10) # Houve desconto de 10% aqui

else:
    totalComDesconto = totalSemDesconto - totalSemDesconto * (0.15) # Houve desconto de 15% aqui, pois a quantidade do produto é maior ou igual a 1000

print('O valor total sem deconto é de: R$ {:.2f}'.format(totalSemDesconto))
print('O valor total com desconto é de: R$ {:.2f}'.format(totalComDesconto))

