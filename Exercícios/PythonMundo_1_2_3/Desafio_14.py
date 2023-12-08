# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('=' * 6 + ' DESAFIO 14 ' + '=' * 6)

celsius = float(input('[?] - Informe a temperatura em °C: '))
fahrenheit = (celsius * 1.8) + 32

print(f'[!] - A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F')