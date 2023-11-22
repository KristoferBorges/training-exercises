# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

print('{} DESAFIO 05 {}'.format('='*6, '='*6))

numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1

print(f'\n[!] NÚMERO DIGITADO = {numero}\n[!] SUCESSOR = {sucessor}\n[!] ANTECESSOR = {antecessor}')
print('='*24)
