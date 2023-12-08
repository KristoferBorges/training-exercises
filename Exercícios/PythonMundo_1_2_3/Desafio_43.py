# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal 
# (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 43 ' + '=' * 6)

peso = float(input('\n\n[?] - INFORME SEU PESO: '))

if peso < 18.5:
    print(green + f'\n\n[!] - SEU IMC É {peso}, VOCÊ ESTÁ ABAIXO DO PESO' + normal)
elif peso >= 18.5 and peso < 25:
    print(yellow + f'\n\n[!] - SEU IMC É {peso}, VOCÊ ESTÁ COM O PESO IDEAL' + normal)
elif peso >= 25 and peso < 30:
    print(yellow + f'\n\n[!] - SEU IMC É {peso}, VOCÊ ESTÁ COM SOBREPESO' + normal)
elif peso >= 30 and peso <= 40:
    print(yellow + f'\n\n[!] - SEU IMC É {peso}, VOCÊ ESTÁ COM OBESIDADE' + normal)
elif peso > 40:
    print(yellow + f'\n\n[!] - SEU IMC É {peso}, VOCÊ ESTÁ COM OBESIDADE MÓRBIDA' + normal)