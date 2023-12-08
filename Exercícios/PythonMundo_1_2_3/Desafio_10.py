# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('=' * 6 + ' DESAFIO 10 ' + '=' * 6)
real = float(input('Quanto dinheiro você tem na carteira? R$'))

convertivo = real / 4.91

print('Com R${:.2f} você pode comprar U${:.2f} dolares'.format(real, convertivo))
