# Crie um programa que leia dois números e mostre a soma entre eles.

print('====== DESAFIO 03 ======')

valores = {
    'n1': float(input('Primeiro número: ')),
    'n2': float(input('Segundo número: '))
}

soma = valores['n1'] + valores['n2']
print(f'\nA soma entre {valores["n1"]} e {valores["n2"]} é igual a {soma}')