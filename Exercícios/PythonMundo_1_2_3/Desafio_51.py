# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 51 ' + '=' * 6 + '\n\n')

termo = int(input('[?] - INFORME O TERMO: '))
razao = int(input('[?] - INFORME A RAZÃO: '))
cont = 0

for c in range(termo, 999, razao):
    if cont == 10:
        break
    else:
        print(f'{c}', end='↦ ')
        cont += 1
print('ACABOU')