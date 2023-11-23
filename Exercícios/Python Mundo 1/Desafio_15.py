# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=' * 6 + ' DESAFIO 15 ' + '=' * 6)

dias = int(input('[?] - Quantos dias alugados? '))
km = float(input('[?] - Quantos Km rodados? '))
preco = (dias * 60) + (km * 0.15)

print(f'[!] - O total a pagar é de R${preco:.2f}')