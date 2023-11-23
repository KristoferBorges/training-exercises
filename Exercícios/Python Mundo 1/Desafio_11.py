# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('=' * 6 + ' DESAFIO 11 ' + '=' * 6)

largura = float(input('[?] - Informe a largura da parede: '))
altura = float(input('[?] - Informe a altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'\n[!] - Largura: {largura:.2f}m')
print(f'[!] - Altura: {altura:.2f}m')
print(f'[!] - Área Total: {area:.2f}m²')
print(f'[!] - Tinta necessária para pintar o espaço: {tinta:.2f}L')
