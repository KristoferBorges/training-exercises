# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 47 ' + '=' * 6)

for n in range(1, 50 + 1):
    if n % 2 == 0:
        print(n, end=', ')
print('FIM')