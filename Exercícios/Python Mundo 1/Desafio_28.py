# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print('=' * 6 + ' DESAFIO 28 ' + '=' * 6)



print('=' * 6 + ' TENTE ADIVINHAR O NÚMERO ' + '=' * 6)
while True:
    numero = randint(0, 5)
    escolha = int(input("\n[?] - QUAL NÚMERO ESTOU PENSANDO?: "))
    if escolha == numero:
        print('[!] - VOCÊ ACERTOU')
        break
    else:
        print('[!] - VOCÊ ERROU')
        print(f'[!] - O NÚMERO QUE EU ESTAVA PENSANDO ERA {numero}')
        print('[!] - TENTE NOVAMENTE')
        sleep(1)
    
    op = input('[?] - DESEJA CONTINUAR? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break

print('\n[!] - OBRIGADO POR JOGAR COMIGO')


