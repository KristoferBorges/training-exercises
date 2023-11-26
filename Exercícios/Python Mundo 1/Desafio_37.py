# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 37 ' + '=' * 6)

numero = int(input(yellow + '\n\n[?] - INFORME UM NÚMERO PARA CONVERSÃO: '))
print('[ 1 ] - CONVERSÃO EM BINÁRIO.')
print('[ 2 ] - CONVERSÃO EM OCTAL.')
print('[ 3 ] - CONVERSÃO EM HEXADECÍMAL.\n')
op = int(input('[?] - ESCOLHA UMA OPÇÃO: '))

if op == 1:
    convertido = bin(numero)
    print(green + f'\n[!] - O VALOR [{numero}] CONVERTIDO EM BINÁRIO É = [{convertido[2:]}]' + normal)
elif op == 2:
    convertido = oct(numero)
    print(green + f'\n[!] - O VALOR [{numero}] CONVERTIDO EM OCTAL É = [{convertido[2:]}]' + normal)
elif op == 3:
    convertido = hex(numero)
    print(green + f'\n[!] - O VALOR [{numero}] CONVERTIDO EM HEXADECÍMAL É = [{convertido[2:]}]' + normal)
else:
    print(red + '[!] - OPÇÃO INVÁLIDA!' + normal)