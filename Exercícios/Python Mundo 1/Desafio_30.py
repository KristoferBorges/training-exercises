# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 30 ' + '=' * 6)

while True:
    numero = int(input(green + '\n\n[?] - DIGITE UM NÚMERO PARA VERIFICAR SE É IMPAR OU PAR: '))

    if numero % 2 == 0:
        print(yellow + f'[!] - O NÚMERO [{numero}] É PAR!' + normal)
    else:
        print(yellow + f'[!] - O NÚMERO [{numero}] É IMPAR!' + normal)
    
    op = input('[?] - QUER CONTINUAR? [S/N]' + normal).upper().strip()

    if op == 'N':
        break
