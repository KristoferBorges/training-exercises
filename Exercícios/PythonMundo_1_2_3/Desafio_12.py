# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('=' * 6 + ' DESAFIO 12 ' + '=' * 6)

preco = float(input('[?] - Informe o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print(f'[!] - O valor do protudo é de R${preco:.2f}, porém, com o nosso desconto de [5%] o valor final fica de R${desconto:.2f}')