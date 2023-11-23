# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

print('=' * 6 + ' DESAFIO 17 ' + '=' * 6)

adj = float(input('[?] - CATETO ADJACENTE: '))
oposto = float(input('[?] - CATETO OPOSTO: '))

hipotenusa = hypot(adj, oposto)

print(f'\n[!] - O COMPRIMENTO DO CATETO OPOSTO É [{oposto:.2f}]')
print(f'[!] - O COMPRIMENTO DO CATETO ADJACENTE É [{adj:.2f}]')
print(f'[!] - SUA HIPOTENUSA É [{hipotenusa:.2f}]')