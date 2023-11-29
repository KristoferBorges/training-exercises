# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 49 ' + '=' * 6 + '\n\n')

print('=*' * 5 + ' TABUADA ' + '*=' * 5)
numero = int(input('[?] - INFORME UM NÚMERO PARA TABUAR: '))

for c in range(1, 10 + 1):
    print('{} x {:2} = {}'.format(numero, c, c * numero))
print(yellow + '\n FIM DA TABUADA' + normal)