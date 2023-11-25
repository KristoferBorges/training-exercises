# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 32 ' + '=' * 6)

ano = int(input(yellow + '\n\n[?] - INFORME UM ANO PARA VERIFICAR SE É BISSEXTO: ' + normal))

if ano % 4 == 0 or ano % 400 == 0 :
    if ano % 100 == 0:
        print(red + f'[!] - O ANO [{ano}] NÃO É BISSEXTO' + normal)
    else:
        print(green + f'[!] - O ANO [{ano}] É BISSEXTO!' + normal)
else:
    print(red + f'[!] - O ANO [{ano}] NÃO É BISSEXTO' + normal)