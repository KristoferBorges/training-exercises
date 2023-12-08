# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('====== DESAFIO 04 ======')

inputUsuario = input('Digite algo: ')

print(f'[!] - Seu tipo primitivo é = [{type(inputUsuario)}]')
print(f'[!] - Só tem espaços? = [{inputUsuario.isspace()}]')
print(f'[!] - É um número? = [{inputUsuario.isnumeric()}]')
print(f'[!] - É alfabético? = [{inputUsuario.isalpha()}]')
print(f'[!] - É alfanumérico? = [{inputUsuario.isalnum()}]')
print(f'[!] - Está em maiúsculas? = [{inputUsuario.isupper()}]')
print(f'[!] - Está em minúsculas? = [{inputUsuario.islower()}]')
print(f'[!] - Está capitalizada? = [{inputUsuario.istitle()}]')
