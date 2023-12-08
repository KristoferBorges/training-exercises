palavra = str(input('[?] - INFORME UMA PALAVRA/FRASE: '))
if palavra.strip().replace(' ', '') == palavra[::-1].strip().replace(' ', ''):
    print('\n\t[!] - É UM PALÍNDROMO')
else:
    print('\n\t[!] - NÃO É UM PALÍNDROMO')