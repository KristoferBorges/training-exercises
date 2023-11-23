# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

print('=' * 6 + ' DESAFIO 19 ' + '=' * 6)

aluno1 = input('[?] - DIGITE O NOME DO PRIMEIRO ALUNO: ')
aluno2 = input('[?] - DIGITE O NOME DO SEGUNDO ALUNO: ')
aluno3 = input('[?] - DIGITE O NOME DO TERCEIRO ALUNO: ')
aluno4 = input('[?] - DIGITE O NOME DO QUARTO ALUNO: ')

escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print(f'\n[!] - O ESCOLHIDO PARA APAGAR O QUADRO FOI [{escolhido}]')