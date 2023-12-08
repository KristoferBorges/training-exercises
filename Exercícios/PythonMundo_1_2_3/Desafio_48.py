# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 48 ' + '=' * 6)

somaMultiplos = 0
somaNumeros = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        somaNumeros = somaNumeros + 1
        somaMultiplos = somaMultiplos + c
print(f'[!] - A SOMA DE TODOS OS NÚMEROS ÍMPARES {somaNumeros} VALORES É: {somaMultiplos}')