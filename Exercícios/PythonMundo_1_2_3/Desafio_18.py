# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
import numpy as np

print('=' * 6 + ' DESAFIO 18 ' + '=' * 6)

angulo = int(input('[?] - DIGITE UM ÂNGULO: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'[!] - SENO = [{seno:.2f}]')
print(f'[!] - COSSENO = [{cosseno:.2f}]')
print(f'[!] - TANGENTE - [{tangente:.2f}]')