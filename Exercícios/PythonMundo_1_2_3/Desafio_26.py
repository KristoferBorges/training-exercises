# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição 
# ela aparece a primeira vez e em que posição ela aparece a última vez.

print('=' * 6 + ' DESAFIO 26 ' + '=' * 6)

frase = input('DIGITE UMA FRASE: ').upper().strip()
qntA = frase.count('A')

print(f'\n[!] - QUANTIDADE DE [A] = {qntA}')
print(f'[!] - PRIMEIRO [A] VISTO = ', frase.find('A'))
print(f'[!] - ÚLTIMO [A] VISTO = ', frase.find('A', -1))
