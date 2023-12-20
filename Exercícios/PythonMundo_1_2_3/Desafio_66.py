qntNumbers = 0
somaNumbers = 0

while (True):
    number = int(input('[!] - INFORME UM NÚMERO: '))

    if (number == 999):
        break
    else:
        qntNumbers = qntNumbers + 1
        somaNumbers = somaNumbers + number

print(f'- QUANTIDADE DE NÚMEROS [{qntNumbers}]')
print(f'- VALOR TOTAL SOMADO [{somaNumbers}]')
