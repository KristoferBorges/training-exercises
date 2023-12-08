# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 46 ' + '=' * 6)

for n in range(10, 0, -1):
    print(n)
    sleep(1)
print(red + '\nBUM ' + yellow + ' BUM ' + green + ' BUM ' + normal + ' POOL ')
