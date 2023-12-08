# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 38 ' + '=' * 6)

n1 = int(input(yellow + '\n\n[?] - DIGITE UM NÚMERO: ' + normal))
n2 = int(input(yellow + '[?] - DIGITE UM NÚMERO: ' + normal))

print(f'\n\n[!] - O PRIMEIRO VALOR É: {n1}')
print(f'[!] - O SEGUNDO VALOR É: {n2}')

if n1 > n2:
    print(green + '\n\n[!] - O PRIMEIRO VALOR É MAIOR QUE O SEGUNDO!' + normal)
elif n2 > n1:
    print(green + '\n\n[!] - O SEGUNDO VALOR É MAIOR QUE O PRIMEIRO!' + normal)
elif n1 == n2:
    print(green + '\n\n[!] - OS NÚMEROS SÃO IGUAIS' + normal)