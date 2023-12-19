n1 = 0
n2 = 1
n3 = 0

termo = int(input('INFORME UM NÚMERO PARA VER SUA SEQUÊNCIA FIBONACCI: '))
cont = 0

while (cont < termo):
    print(f'{n1}, {n2}, {n3}', end='')
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    cont = cont + 1
