# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador 
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 58 ' + '=' * 6 + '\n\n')

cont = 1
choiceComputer = randint(1, 5)

choicePlayer = int(input('[?] - TENTE ADIVINHAR O NÚMERO QUE EU ESTOU PENSANDO: '))

while choicePlayer != choiceComputer:
    cont = cont + 1
    choicePlayer = int(input('\n[?] - VOCÊ ERROU, TENTEDE OUTRA VEZ: '))

print(green + f'\n\n[!] - VOCÊ ACERTOU, FORAM NECESSÁRIAS [{cont}] TENTATIVAS!' + normal)