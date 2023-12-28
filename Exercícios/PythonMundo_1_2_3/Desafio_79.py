from modulo import Printador

print('=' * 6 + ' DESAFIO 79 ' + '=' * 6 + '\n\n')

lista = list()

while True:
    number = int(input(f'\nINFORME O VALOR PARA ADICIONAR NA LISTA: '))
    if number not in lista:
        print("\nITEM ADICIONADO NA LISTA!")
        lista.append(number)
    else:
        print("\nITEM DUPLICADO, ESCOLHA OUTRO NÚMERO!")
    
    escolha = str(input("DESEJA CONTINUAR? [S/N]: ").strip().upper()[0])

    if escolha == "N":
        break

lista.sort()
print(f"SUA LISTA CONTÉM OS NÚMEROS: {lista}")