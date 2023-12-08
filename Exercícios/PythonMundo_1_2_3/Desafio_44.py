# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 44 ' + '=' * 6)

produto = float(input('\n\n[?] - INFORME O VALOR DO PRODUTO: '))
print('\n\n[1] - À VISTA DINHEIRO/CHEQUE')
print('[2] - À VISTA NO CARTÃO')
print('[3] - EM ATÉ 2X NO CARTÃO')
print('[4] - 3X OU MAIS NO CARTÃO')

opcao = int(input('\n\n[?] - ESCOLHA UMA OPÇÃO: '))

if opcao == 1:
    produtoDesconto = produto - (produto * 0.1)
    print(green + f'\n[!] - VOCÊ ESCOLHEU A OPÇÃO DE [DINHEIRO/CHEQUE], ASSIM, O VALOR DO PRODUTO FICARÁ {produtoDesconto:.2f}' + normal)
elif opcao == 2:
    produtoDesconto = produto - (produto * 0.05)
    print(green + f'\n[!] - VOCÊ ESCOLHEU A OPÇÃO DE [À VISTA NO CARTÃO], ASSIM, O VALOR DO PRODUTO FICARÁ {produtoDesconto:.2f}' + normal)
elif opcao == 3:
    produtoDesconto = produto
    print(green + f'\n[!] - VOCÊ ESCOLHEU A OPÇÃO DE [EM ATÉ 2X NO CARTÃO], ASSIM, O VALOR DO PRODUTO FICARÁ {produtoDesconto:.2f}' + normal)
    print(green + f'[!] - O VALOR DA PARCELA SERÁ DE {produtoDesconto / 2:.2f}' + normal)
elif opcao == 4:
    produtoDesconto = produto + (produto * 0.2)
    print(green + f'\n[!] - VOCÊ ESCOLHEU A OPÇÃO DE [3X OU MAIS NO CARTÃO], ASSIM, O VALOR DO PRODUTO FICARÁ {produtoDesconto:.2f}' + normal)
    parcelas = int(input('\n[?] - INFORME A QUANTIDADE DE PARCELAS: '))
    if parcelas >= 3:
        print(green + f'[!] - O VALOR DA PARCELA SERÁ DE {produtoDesconto / parcelas:.2f}' + normal)
    else:
        print(red + '[!] - VOCÊ NÃO ESCOLHEU UMA QUANTIDADE VÁLIDA DE PARCELAS' + normal)
        