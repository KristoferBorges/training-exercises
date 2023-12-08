# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 39 ' + '=' * 6)

dataAtual = datetime.datetime.now()
anoAtual = dataAtual.year

nascimentoJovem = int(input('\n\n[?] - EM QUE ANO VOCÊ NASCEU: '))
anoAlistamento = nascimentoJovem + 18
anoJovem = anoAtual - nascimentoJovem

if anoJovem > 18:
    anosDiferenca = anoJovem - 18
    print(green + f'\n\n[!] - QUEM NASCEU EM {nascimentoJovem} TEM {anoJovem} EM {anoAtual}!')
    print(f'[!] - VOCÊ DEVERIA TER SE ALISTADO  HÁ {anosDiferenca}!')
    print(f'[!] - SEU ALISTAMENTO FOI EM {anoAlistamento}' + normal)
elif anoJovem < 18:
    anosDiferenca = abs(anoJovem - 18)
    print(green + f'[!] - QUEM NASCEU EM {nascimentoJovem} TEM {anoJovem} EM {anoAtual}!')
    print(f'[!] - AINDA FALTAM {anosDiferenca} ANOS PARA SEU ALISTAMENTO')
    print(f'[!] - SEU ALISTAMENTO SERÁ EM {anoAlistamento}' + normal)
elif anoJovem == 18:
    print(green + f'[!] - QUEM NASCEU EM {nascimentoJovem} TEM {anoJovem} EM {anoAtual}!')
    print(red + '[!] - VOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE!' + normal)

