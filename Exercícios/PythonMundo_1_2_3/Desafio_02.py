# Crie um script python que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

print('====== DESAFIO 02 ======')

nascimento = {
    'dia': input('Dia: '),
    'mes': input('Mês: '),
    'ano': input('Ano: ')
}

print(f'Você nasceu no dia {nascimento["dia"]} de {nascimento["mes"]} de {nascimento["ano"]}, Correto?')