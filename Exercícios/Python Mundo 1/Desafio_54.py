# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram 
# a maioridade e quantas já são maiores.

import datetime

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 54 ' + '=' * 6 + '\n\n')

pessoasJovens = 0
pessoasVelhas = 0
data = datetime.datetime.now()
anoAtual = data.year

for pessoa in range(1, 7 + 1):
    nascimento = int(input(yellow + f'[?] - QUAL O ANO DE NASCIMENTO DA {pessoa}º PESSOA? ' + normal))

    anos = anoAtual - nascimento
    if anos >= 18:
        pessoasVelhas = pessoasVelhas + 1
    elif anos < 18:
        pessoasJovens = pessoasJovens + 1

print(green + f'[!] - TEMOS NA LISTAGEM {pessoasVelhas} PESSOAS VELHAS!' + normal)
print(green + f'[!] - TEMOS NA LISTAGEM {pessoasJovens} PESSOAS JOVENS!' + normal)
