# Um conjunto de caixas é numerado em ordem crescente usando adesivos que contém algarismos
# individuais. Para se numerar a caixa de índice 10, são usados 2 adesivos, por exemplo.
# O orçamento para a aquisição de adesivos é limitado, então deseja-se conhecer número máximo de caixas que podem ser numerados,
# de 1 até um determinado valor, sem pular nenhum número na contagem, dado esse limite.
# Escreva um algoritmo que receba o número total de adesivos disponíveis e retorne o número máximo de caixas que podem ser numerados.

#Ex: Se tivermos 5 adesivos disponíveis, podemos numerar 5 caixas.


adesivo = int(input('Informe a quantidade de adesivos disponível:'))
valor = int(adesivo - 9)


if (adesivo >= 0) and (adesivo <= 9):
        caixa = adesivo

if adesivo >= 9:
    caixa = int (((9) + valor/2))

print('A quantidade de caixas que podemos numerar é: {}'.format(caixa))