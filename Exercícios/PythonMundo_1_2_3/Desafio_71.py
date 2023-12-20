green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 71 ' + '=' * 6 + '\n\n')

notas50 = 0
notas20 = 0
notas10 = 0
notas01 = 0
print("=-" * 24)
print("\t\tBANCO KAKAROTO")
print("=-" * 24)
valorDoSaque = int(input("[?] - INFORME QUANTO QUER SACAR: "))

while valorDoSaque != 0:
    if valorDoSaque % 50 == 0:
        notas50 = notas50 + 1
        valorDoSaque = valorDoSaque - 50
    elif valorDoSaque % 20 == 0:
        notas20 = notas20 + 1
        valorDoSaque = valorDoSaque - 20
    elif valorDoSaque % 10 == 0:
        notas10 = notas10 + 1
        valorDoSaque = valorDoSaque - 10
    elif valorDoSaque % 1 == 0:
        notas01 = notas01 + 1
        valorDoSaque = valorDoSaque - 1

print("\n\n")
print("=-" * 24)
print("\t\tVALORES DE CÉDULAS")
print("=-" * 24)
print(f"NOTAS DE 50 = [{notas50}]")
print(f"NOTAS DE 20 = [{notas20}]")
print(f"NOTAS DE 10 = [{notas10}]")
print(f"NOTAS DE 01 = [{notas01}]")