# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

print('=' * 6 + ' DESAFIO 16 ' + '=' * 6)

numero = float(input('\n[?] - DIGITE UM NÚMERO E EU IREI TRUNCA-LO: '))
numero = trunc(numero)
print(f'[!] - O NUMERO TRUNCADO FICA = [{numero}]')