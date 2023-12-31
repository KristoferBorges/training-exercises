from modulo import Printador

print('=' * 6 + ' DESAFIO 73 ' + '=' * 6 + '\n\n')

Printador.centralizador(Printador.green + "TIMES DO CAMPEONATO BRASILEIRO DE FUTEBOL" + Printador.normal)

times_de_futebol = (
    "Flamengo",
    "Chapecoense",
    "Palmeiras",
    "Santos",
    "São Paulo",
    "Corinthians",
    "Grêmio",
    "Internacional",
    "Atlético Mineiro",
    "Cruzeiro",
    "Fluminense",
    "Botafogo",
    "Vasco da Gama",
    "Bahia",
    "Sport",
    "Fortaleza",
    "Ceará",
    "Athletico Paranaense",
    "Coritiba",
    "Goias"
)

Printador.centralizador("OS 5 PRIMEIROS TIMES SÃO:")

cont = 1
for time in times_de_futebol:
    print(f"\t{cont}º lugar [{time}]")
    cont += 1
    if cont == 6:
        break

Printador.centralizador("OS 4 ÚLTIMOS COLOCADOS SÃO:")
cont2 = 20
for i in range(-1, -5, -1):
    print(f"\t{cont2}º lugar [{times_de_futebol[i]}]")
    cont2 -= 1

Printador.centralizador("OS TIMES EM ORDEM ALFABÉTICA")

times_de_futebolAlfabetico = tuple(sorted(times_de_futebol))
qntTimes = len(times_de_futebol)

for time in range(1, qntTimes):
    primeiraLetra = times_de_futebolAlfabetico[time][0]
    print(f"\t{primeiraLetra} - {times_de_futebolAlfabetico[time]}")

Printador.centralizador("A POSIÇÃO DO CHAPECOENSE É:")
indexChapecoense = times_de_futebol.index("Chapecoense") + 1
print(f"\tA POSIÇÃO DO CHAPECOENSE É [{indexChapecoense}º]")