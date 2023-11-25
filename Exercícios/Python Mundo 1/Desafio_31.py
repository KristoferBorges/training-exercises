# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 31 ' + '=' * 6)

distancia = float(input(green + '\n\n[?] - INFORME A DISTÂNCIA DA VIAGEM: ' + normal))
tipoViagem = input('[?] - PREMIUM OU NORMAL? [P/N]').upper().strip()

if distancia > 200.00:
    valorTotal = distancia * 0.45
    if tipoViagem == "P":
        valorTotal = valorTotal + (valorTotal * 15 / 100)
else:
    valorTotal = distancia * 0.50
    if tipoViagem == "P":
        valorTotal = valorTotal + (valorTotal * 15 / 100)


print(yellow + '[!] - O VALOR DA VIAGEM = ' + green + f'[R${valorTotal:.2f}]')
