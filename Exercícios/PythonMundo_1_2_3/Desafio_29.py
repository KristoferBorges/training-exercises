# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 29 ' + '=' * 6)

velocidade = int(input(yellow + '\n[!] - INFORME A VELOCIDADE DO CARRO: ' + normal))

if velocidade > 80:
    ultrapassado = velocidade - 80
    valorTotal = ultrapassado * 7
    print(red + '\n\n[!] - VOCÊ SERÁ MULTADO POR ULTRAPASSAR O LIMITE MÁXIMO PERMITIDO!')
    print(f'[!] - O VALOR TOTAL É [R${valorTotal:.2f}]' + normal)
else:
    print(green + f'[!] - VOCÊ ESTAVA DENTRO DO LIMITE, PODE SEGUIR!' + normal)

