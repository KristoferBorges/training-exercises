# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('=' * 6 + ' DESAFIO 27 ' + '=' * 6)

nomeCompleto = input('\n[?] - DIGITE SEU NOME COMPLETO: ').strip()

primeiroNome = nomeCompleto.split()[0]
ultimoNome = nomeCompleto.split()[-1]

print(f'\n[!] - PRIMEIRO NOME: {primeiroNome}')
print(f'[!] - ÚLTIMO NOME: {ultimoNome}')