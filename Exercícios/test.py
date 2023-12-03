from datetime import datetime

dataAtual = datetime.now()

# Usando strftime para formatar a data como uma string
dataComparadaa = datetime(2023, 12, 2)
dataComparada = datetime.strptime(dataComparadaa.strftime("%d/%m/%Y"), "%d/%m/%Y")

if dataAtual.date() > dataComparada.date():
    print('DESATIVADO')
elif dataAtual.date() < dataComparada.date():
    print('ATIVADO')
elif dataAtual.date() == dataComparada.date():
    print('IGUAL, ATIVADO')

print(dataAtual.date(), dataComparada.date())