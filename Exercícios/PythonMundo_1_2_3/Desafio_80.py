from modulo import Printador

lista = list()

for i in range(0, 5 + 1):
    number = int(input("\nDIGITE UM VALOR: "))

    while (number in lista):
        print("[!] - ESSE NÚMERO JÁ EXISTE NA LISTA!")
        number = int(input("DIGITE OUTRO VALOR: "))

    if i == 0:
        lista.append(number)
        print("\nO PRIMEIRO VALOR FOI ADICIONADO AO FINAL DA LISTA")
    else:
        if (number > max(lista)):
            lista.append(number)
            print(f"\nO VALOR FOI INSERIDO NA POSIÇÃO {lista.index(number)}º")
        elif (number < min(lista)):
            lista.insert(0, number)
            print(f"\nO VALOR FOI INSERIDO NA POSIÇÃO {lista.index(number)}º")
        else:
            for ind, num in enumerate(lista):
                if number <= num:
                    lista.insert(ind, number)
                    print(f"\nO VALOR FOI INSERIDO NA POSIÇÃO {ind}º")
                    break

print("=" * 30)
listaOrdenada = lista[:]
listaOrdenada.sort()
print(f"\nVALORES ORDENADOS USANDO FUNÇÃO SORT({listaOrdenada})")
print(f"VALORES ORDENADOS USANDO O PROCESSO DE LÓGICA E ANÁLISE {lista}")