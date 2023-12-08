# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 52 ' + '=' * 6 + '\n\n')

for _ in range(1, 10 + 1):
    numero = int(input('\n\n[?] - INFORME UM NÚMERO, VOU VERIFICAR SE É PRIMO OU NÃO: '))
    cont = 0
    for c in range(1, numero + 1, 1):
        if numero % c == 0:
            cont += 1

    if cont > 2 or cont <= 1:
        print(f'[!] O NÚMERO [{numero}] NÃO É PRIMO!')
    else:
        print(f'[!] - O NÚMERO [{numero}] É UM NÚMERO PRIMO!')