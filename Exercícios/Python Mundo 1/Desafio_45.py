# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 45 ' + '=' * 6)

tentativas = 0
while True:
    computadorChoice = random.choice(['Tesoura', 'Papel', 'Pedra'])

    print('\n\n[1] - PEDRA')
    print('[2] - PAPEL')
    print('[3] - TESOURA')

    playerChoice = input('[?] - ESCOLHA ENTRE AS OPÇÕES PARA JOGAR: ')

    print('\n\n[!] - JO')
    sleep(0.7)
    print('[!] - KEN')
    sleep(0.5)
    print('[!] - PÔ')
    sleep(0.3)

    if playerChoice == '1':
        playerChoice = 'Pedra'
        if computadorChoice == 'Papel':
            print(red + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ PERDEU' + normal)
        elif computadorChoice == 'Tesoura':
            print(green + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ GANHOU' + normal)
        elif computadorChoice == 'Pedra':
            print(yellow + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, EMPATE' + normal)

    elif playerChoice == '2':
        playerChoice = 'Papel'
        if computadorChoice == 'Tesoura':
            print(red + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ PERDEU' + normal)
        elif computadorChoice == 'Pedra':
            print(green + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ GANHOU' + normal)
        elif computadorChoice == 'Papel':
            print(yellow + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, EMPATE' + normal)

    elif playerChoice == '3':
        playerChoice = 'Tesoura'
        if computadorChoice == 'Pedra':
            print(red + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ PERDEU' + normal)
        elif computadorChoice == 'Papel':
            print(green + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, VOCÊ GANHOU' + normal)
        elif computadorChoice == 'Tesoura':
            print(yellow + f'\n\n[!] - VOCÊ ESCOLHEU {playerChoice} E O COMPUTADOR ESCOLHEU {computadorChoice}, EMPATE' + normal)

    else:
        print(red + '\n\n[!] - VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA' + normal)

    if tentativas == 5:
        op = input('\n\n[?] - DESEJA JOGAR NOVAMENTE? [S/N]: ').upper()
        if op == 'N':
            print(green + '\n\n[!] - OBRIGADO POR JOGAR' + normal)
            break
        else:
            tentativas = 0

    tentativas += 1