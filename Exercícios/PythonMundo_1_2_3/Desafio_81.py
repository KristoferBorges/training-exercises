from modulo import Printador

print('=' * 6 + ' DESAFIO 81 ' + '=' * 6 + '\n\n')

list_numbers = list()
have_numberFive = False

while True:
    number = int(input("INFORME UM NÚMERO: "))
    if number == 999:
        break

    while number in list_numbers:
        number = int(input("ESSE NÚMERO JÁ ESTÁ NA LISTA!\n > INFORME OUTRO NÚMERO: "))
        if number == 999:
            break

    if number == 5:
        have_numberFive = True
    
    list_numbers.append(number)

listaOrdenada = list_numbers[:]
listaOrdenada.sort(reverse=True)
print(f"NA LISTA TEMOS {len(list_numbers)} NÚMEROS")
print(f"OS VALORES NA LISTA DECRESCENTE FICAM {listaOrdenada}")
if have_numberFive:
    print("NA LISTA NÓS TEMOS O NÚMERO 5")
else:
    print("NA LISTA NÓS NÃO TEMOS O NÚMERO 5")