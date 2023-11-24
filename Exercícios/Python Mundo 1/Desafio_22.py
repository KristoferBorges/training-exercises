# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

print('=' * 6 + ' DESAFIO 22 ' + '=' * 6)

nome = str(input('[?] - DIGITE SEU NOME: '))

nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
qntLetras = len(nome.replace(' ', ''))
primeiroNome = nome.split()[0]
qntLetrasPrimeiro = len(nome.split()[0])

print(f'\n[!] - SEU NOME MAIÚSCULO: {nomeMaiusculo}')
print(f'[!] - SEU NOME MINÚSCULO: {nomeMinusculo}')
print(f'[!] - SEU NOME INTEIRO TEM: [{qntLetras}] LETRAS')
print(f'[!] - SEU PRIMEIRO NOME É [{primeiroNome}] E TEM [{qntLetrasPrimeiro}] LETRAS')