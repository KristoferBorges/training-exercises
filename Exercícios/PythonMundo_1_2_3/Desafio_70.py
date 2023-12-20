green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 70 ' + '=' * 6 + '\n\n')

totalGasto = 0
valoresAcimaDe1000 = 0
produtoMaisBarato = 0
qntProdutos = 1

escolha = "S"
while (escolha == "S"):
    # Coleta de dados
    nomeProduto = str(input("[?] - INFORME O VALOR DO PRODUTO: ").strip().upper())
    valorProduto = float(input("[?] - INFORME O VALOR DO PRODUTO: ").strip())

    # Coleta do valor total gasto
    totalGasto = totalGasto + valorProduto

    # Coleta de produtos acima de 1000
    if valorProduto > 1000:
        valoresAcimaDe1000 = valoresAcimaDe1000 + 1
    
    # Coleto do produto mais barato
    if qntProdutos == 1:
        produtoMaisBarato = valorProduto
    elif (valorProduto < produtoMaisBarato):
        produtoMaisBarato = valorProduto
    else:
        continue

    # Contagem dos produtos
    qntProdutos = qntProdutos + 1

    # Escolha de continuar
    escolha = str(input("[?] - DESEJA CONTINUAR [S/N]: ").upper()[0])
