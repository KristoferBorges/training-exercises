# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('{} DESAFIO 09 {}'.format('='*6, '='*6))

numero = int(input('Digite um número: '))
print('='*24)
print(f'\n[!] TABUADA DO [{numero}]')
print('='*24)
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 1, "=", numero*1))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 2, "=", numero*2))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 3, "=", numero*3))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 4, "=", numero*4))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 5, "=", numero*5))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 6, "=", numero*6))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 7, "=", numero*7))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 8, "=", numero*8))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 9, "=", numero*9))
print('{:<2} x {:>2} {:>2} {:>3}'.format(numero, 10, "=", numero*10))
print('='*24)

