# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('{} DESAFIO 006 {}'.format('='*6, '='*6))

numero = float(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'\n[!] NÚMERO DIGITADO = {numero}\n[!] DOBRO = {dobro}\n[!] TRIPLO = {triplo}\n[!] RAIZ QUADRADA = {raiz:.2f}')
print('='*24)