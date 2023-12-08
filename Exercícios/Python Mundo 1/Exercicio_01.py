# Desenvolva um script para gerar números da mega sena e mostrar se ganhou com base em uma pré-definição de números

import random
import sys

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

cont = 1
while True:

    if cont == 150001:
        break

    sorteados = random.sample(range(1, 60 + 1), 6)
    megaSena = [8, 25, 34, 38, 41, 56]
    sorteados.sort()

    print('\n' +'=' * 56)
    print(normal + f'\nTENTATIVA = [{cont}°]')
    print(yellow + f'\nSEUS NÚMEROS FORAM = {sorteados}\n' + normal)
    print(yellow + f'OS NÚMEROS DA MEGA SENA FORAM = {megaSena}\n'+ normal)

    print(yellow + f'NUMEROS COM ACERTOS = ', end=' ' + normal)
    acertos = 0
    for n1, n2 in zip(sorteados, megaSena):
        if n1 == n2:
            print(green + f'{n1}', end=' ' + normal)
            acertos += 1
        elif n1 != n2:
            print(red + '#', end=' ' + normal)
            
        if acertos == 6:
            print(green + f'\nVOCÊ GANHOU NA MEGA SENA!!!' + normal)
            print(green + f'VOCÊ GANHOU NA MEGA SENA!!!' + normal)
            print(green + f'VOCÊ GANHOU NA MEGA SENA!!!' + normal)
            sys.exit()
    cont += 1

    

    


