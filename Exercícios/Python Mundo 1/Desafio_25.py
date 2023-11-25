# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('=' * 6 + ' DESAFIO 25 ' + '=' * 6)

nomeCompleto = input('\nDIGITE SEU NOME: ').upper().strip()
teste = 'SILVA' in nomeCompleto
print(teste)