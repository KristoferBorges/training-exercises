# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 53 ' + '=' * 6 + '\n\n')

texto = str(input('[?] - INFORME UMA FRASE OU PALAVRA: ')).strip()
textoAnalise = texto.replace(' ', '')
tamanho = len(texto)

textoAnalisado = ''
for c in range(tamanho - 1, -1, -1):
    # print(textoAnalise[c], end='')
    textoAnalisado = textoAnalisado + textoAnalise[c]

print(f'\n[!] - O SEU TEXTO INICIAL FOI: {texto}')
print(f'[!] - AO CONTRÁRIO FICA {textoAnalisado}')

if textoAnalise == textoAnalisado:
    print(green + '[!] - O TEXTO INFORMADO É UM PALÍNDROMO!' + normal)
else:
    print(red + '[!] - O TEXTO INFORMADO NÃO É UM PALÍNDROMO!' + normal)