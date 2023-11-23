# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('{} DESAFIO 08 {}'.format('='*6, '='*6))

metros = float(input('Digite um valor em metros: '))
quilometros = metros * 0.001
hectometro = metros * 0.01
decametros = metros * 0.1
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

print(f'\n[!] METROS = {metros:.2f}m\n[!] QUILÔMETROS = {quilometros:.3f}km')
print(f'[!] HECTÔMETROS = {hectometro:.2f}hm\n[!] DECÂMETROS = {decametros:.2f}dam\n[!] DECÍMETROS = {decimetros:.2f}dm')
print(f'[!] CENTÍMETROS = {centimetros:.2f}cm\n[!] MILÍMETROS = {milimetros:.2f}mm')