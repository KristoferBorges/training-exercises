# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 55 ' + '=' * 6 + '\n\n')

media = 0
homemMaisVelho = ''
idadeHomemMaisVelho = 0
qntMulheresMenosDeVinte = 0

for pessoa in range(1, 4 + 1):
    nomePessoa = str(input('[?] - NOME: ')).strip()
    idadePessoa = int(input('[?] - IDADE: '))
    sexoPessoa = str(input('[?] - MASCULINO/FEMININO [M/F] ')).upper().strip()

    media = media + idadePessoa

    if sexoPessoa == 'M':
        if pessoa == 1:
            homemMaisVelho = nomePessoa
            idadeHomemMaisVelho = idadePessoa
        elif idadePessoa > idadeHomemMaisVelho:
            homemMaisVelho = nomePessoa
            idadeHomemMaisVelho = idadePessoa
    elif sexoPessoa == 'F':
        if idadePessoa < 20:
            qntMulheresMenosDeVinte = qntMulheresMenosDeVinte + 1

print(f'\n\n[!] - MÉDIA DE IDADE {media / 4}')
print(f'[!] - NOME DO HOMEM MAIS VELHO: {homemMaisVelho}')
print(f'[!] - TEMOS {qntMulheresMenosDeVinte} PESSOA(S) COM MENOS DE 20 ANOS')


