# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print('=' * 6 + ' DESAFIO 24 ' + '=' * 6)

cidade = input('\nDIGITE SUA CIDADE: ').upper().strip()
primeiroNome = cidade.split()[0]
teste = 'SANTO' in primeiroNome
print(teste)

