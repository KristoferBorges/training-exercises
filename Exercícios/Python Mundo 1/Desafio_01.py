# Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de arcodo com o valor digitado.

print('====== DESAFIO 01 ======')

def verificaSexo(nome):
    sexo = nome[-1]
    if sexo =='a':
        sexo = 'bem-vinda'
    elif sexo == 'o':
        sexo = 'bem-vindo'
    else:
        sexo = 'bem-vindo(a)'

    return sexo


nome = input('Qual é seu nome? ')
sexo = verificaSexo(nome)


print('\nOlá', nome + '!', 'Seja ' + sexo + '!')
