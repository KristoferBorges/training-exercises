# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 41 ' + '=' * 6)

idade = int(input('\n\n[?] - INFORME SUA IDADE: '))

if idade <= 9:
    print(green + f'\n\n[!] - VOCÊ TEM {idade} ANOS, SUA CATEGORIA É MIRIM' + normal)
elif idade > 9 and idade <= 14:
    print(yellow + f'\n\n[!] - VOCÊ TEM {idade} ANOS, SUA CATEGORIA É INFANTIL' + normal)
elif idade > 14 and idade <= 19:
    print(yellow + f'\n\n[!] - VOCÊ TEM {idade} ANOS, SUA CATEGORIA É JÚNIOR' + normal)
elif idade > 19 and idade <= 25:
    print(yellow + f'\n\n[!] - VOCÊ TEM {idade} ANOS, SUA CATEGORIA É SÊNIOR' + normal)
elif idade > 25:
    print(yellow + f'\n\n[!] - VOCÊ TEM {idade} ANOS, SUA CATEGORIA É MASTER' + normal)
