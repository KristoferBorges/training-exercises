from modulo import Printador

print('=' * 6 + ' DESAFIO 78 ' + '=' * 6 + '\n\n')

lista = list()
for i in range(0, 4 + 1):
    number = int(input(f"DIGITE UM VALOR PARA A POSIÇÃO {i}º: "))
    lista.append(number)

print("=-" * 15)
maiorNumero = max(lista)
menorNumero = min(lista)

print(f"\nVOCÊ DIGITOU OS NÚMEROS: {lista}")
print(f"O MAIOR VALOR DIGITADO FOI {maiorNumero} NAS POSIÇÕES", end=" ")
for i in range(0, len(lista)):
    if lista[i] == maiorNumero:
        print(f"{i}", end="...")

print(f"\nO MENOR VALOR DIGITADO FOI {menorNumero} NAS POSIÇÕES", end=" ")
for i in range(0, len(lista)):
    if lista[i] == menorNumero:
        print(f"{i}", end="...")