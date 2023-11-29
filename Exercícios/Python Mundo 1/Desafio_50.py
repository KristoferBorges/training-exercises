# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 50 ' + '=' * 6 + '\n\n')

somaPar = 0
cont = 0
for c in range(1, 6 + 1):
    numero = int(input('[?] - INFORME UM NÚMERO: '))
    if numero % 2 == 0:
        somaPar = somaPar + numero
        cont = cont + 1
    else:
        pass

print(f'\n\n[!] - A SOMA ENTRE OS NÚMEROS PARES É: {somaPar}')
print(f'[!] - QUANTIDADE DE NÚMEROS: [{cont}]')