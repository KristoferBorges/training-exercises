# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
# e mostre a ordem sorteada.

import random

print('=' * 6 + ' DESAFIO 20 ' + '=' * 6)

aluno1 = input('[?] - DIGITE O NOME DO PRIMEIRO ALUNO: ')
aluno2 = input('[?] - DIGITE O NOME DO SEGUNDO ALUNO: ')
aluno3 = input('[?] - DIGITE O NOME DO TERCEIRO ALUNO: ')
aluno4 = input('[?] - DIGITE O NOME DO QUARTO ALUNO: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'[!] - A LISTA DE APRESENTAÇÃO É = {lista}')