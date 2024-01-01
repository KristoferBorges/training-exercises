from modulo import Printador

print('=' * 6 + ' DESAFIO 82 ' + '=' * 6 + '\n\n')

listaGeral = list()
listaImpar = list()
listaPar = list()

while True:
    number = int(input("INFORME UM NÚMERO: "))
    if number == 999:
        break

    while number in listaGeral:
        number = int(input("ESSE NÚMERO JÁ FOI ADICIONADO\n [!] INFORME OUTRO NÚMERO: "))
        if number == 999:
            break
    
    listaGeral.append(number)

    if number % 2 == 0:
        listaPar.append(number)
    else:
        listaImpar.append(number)

Printador.centralizador("LISTAS")
print(f"\nLISTA GERAL: {sorted(listaGeral)}")
print(f"\nLISTA DOS ÍMPARES: {sorted(listaImpar)}")
print(f"\nLISTA DOS PARES: {sorted(listaPar)}")