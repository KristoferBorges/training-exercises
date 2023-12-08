# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('=' * 6 + ' DESAFIO 23 ' + '=' * 6)

numero = str(input('[?] - DIGITE UM NÚMERO: '))

print(f'\n[!] NUMERO ESCOLHIDO [{numero}]')

print('[!] - UNIDADE {:.>4}'.format(numero[3]))
print('[!] - DEZENA {:.>4}'.format(numero[2]))
print('[!] - CENTENA {:.>4}'.format(numero[1]))
print('[!] - MILHARE {:.>4}'.format(numero[0]))