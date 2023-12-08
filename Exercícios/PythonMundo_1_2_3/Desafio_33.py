# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 33 ' + '=' * 6)

while True:
    n1 = int(input(green + '\n\n[?] - NÚMERO 1: '))
    n2 = int(input('[?] - NÚMERO 2: '))
    n3 = int(input('[?] - NÚMERO 3: '))

    if n1 >= n2 and n1 >= n3:
        maiorNumero = n1
    elif n2 >= n1 and n2 >= n3:
        maiorNumero = n2
    elif n3 >= n1 and n3 >= n2:
        maiorNumero = n3

    if n1 <= n2 and n1 <= n3:
        menorNumero = n1
    elif n2 <= n1 and n2 <= n3:
        menorNumero = n2
    elif n3 <= n1 and n3 <= n2:
        menorNumero = n3

    print(yellow + f'\n[!] - MAIOR NÚMERO: {maiorNumero}!' + normal)
    print(yellow + f'[!] - MENOR NÚMERO: {menorNumero}!' + normal)

    op = input('\n[?] - DESEJA CONTINUAR? [S/N]').upper().strip()
    if op == "N":
        break