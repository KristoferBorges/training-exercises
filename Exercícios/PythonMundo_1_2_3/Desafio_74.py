import random
from modulo import Printador

Printador.centralizador("ANALISANDO TUPLA")
numeros = tuple()
numeros = random.sample(range(1, 10), 5)

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f"\tOS NÚMEROS FORAM = {numeros}")
print(f"\tO MAIOR NÚMERO É = {maiorNumero}")
print(f"\tO MENOR NÚMERO É = {menorNumero}")