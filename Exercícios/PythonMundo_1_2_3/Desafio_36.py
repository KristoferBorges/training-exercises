# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 36 ' + '=' * 6)

valorCasa = float(input(yellow + '\n\n[?] - INFORME O VALOR DA CASA: ' + normal))
salarioCliente = float(input(yellow + '[?] - QUAL O SALÁRIO DO CLIENTE: ' + normal))
anosEmprestimo = int(input(yellow + '[?] - ANOS PARA PAGAR O EMPRÉSTIMO: ' + normal))

mesesEmprestimo = anosEmprestimo * 12
valorMensal = valorCasa / mesesEmprestimo
analiseCliente = salarioCliente * 0.30

if analiseCliente > valorMensal:
    print(green + '\n[!] - O EMPRÉSTIMO FOI APROVADO!')
    print(green + f'[!] - VALOR TOTAL = [R$ {valorCasa:.2f}]')
    print(green + f'[!] - VALOR DA PARCELA = [R$ {valorMensal:.2f}]')
    print(green + f'[!] - QUANTIDADE DE PARCELAS = [{mesesEmprestimo}] Meses')
else:
    print(red + '[!] - O EMPRÉSTIMO FOI NEGADO PELO SISTEMA!')
