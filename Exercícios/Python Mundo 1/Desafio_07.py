# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('{} DESAFIO 07 {}'.format('='*6, '='*6))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'\n[!] PRIMEIRA NOTA = {nota1}\n[!] SEGUNDA NOTA = {nota2}\n[!] MÉDIA = {media:.2f}')
print('='*24)