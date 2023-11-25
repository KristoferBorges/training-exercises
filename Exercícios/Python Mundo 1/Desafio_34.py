# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 34 ' + '=' * 6)

salario = float(input(yellow + '\n\n[?] - INFORME SEU SALÁRIO: ' + normal))


if salario > 1250.00:
    novoSalario = salario + (salario * 10 / 100)
else:
    novoSalario = salario + (salario * 15 / 100)

print(green + f'\n[!] - SEU NOVO SALÁRIO = [{novoSalario:.2f}]' + normal)