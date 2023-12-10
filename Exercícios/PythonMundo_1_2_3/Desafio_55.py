# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 55 ' + '=' * 6 + '\n\n')

for pessoa in range(1, 5 + 1):
    peso = float(input(yellow + f'[?] - INFORME O PESO DA {pessoa}º PESSOA: '))

    if pessoa == 1:
        maiorPeso = peso
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso

print(green + f'\n\nO MAIOR PESO LIDO FOI {maiorPeso:.2f}' + normal)
print(green + f'O MENOR PESO LIDO FOI {menorPeso:.2f}' + normal)
