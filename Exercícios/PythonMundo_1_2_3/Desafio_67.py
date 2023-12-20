while (True):
    number = int(input("INFORME UM NÚMERO PARA TABUADA: "))
    if number < 0:
        break
    else:
        for n in range(1, 10 + 1):
            print(f'{number} x {n} = {number * n}')

