# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação 
# novamente até ter um valor correto.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 57 ' + '=' * 6 + '\n\n')

sexo = str(input('[?] - INFORME SEU SEXO [M/F]')).strip().upper()
while sexo not in "MF":
    sexo = str(input('[!] - DIGITE APENAS [M/F]: ')).strip().upper()

print('[!] - FIM DO PROGRAMA')