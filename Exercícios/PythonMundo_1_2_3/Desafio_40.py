# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 40 ' + '=' * 6)

nota1 = float(input('\n\n[?] - INFORME SUA PRIMEIRA NOTA: '))
nota2 = float(input('[?] - INFORME SUA SEGUNDA NOTA: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(green + f'\n\n[!] - SUA MÉDIA FOI {media}, VOCÊ PASSOU POIS ESTÁ ACIMA DE 7.0' + normal)
elif media >= 5 and media < 7:
    print(yellow + f'\n\n[!] - SUA MÉDIA FOI {media}, VOCÊ NÃO PASSOU POIS ESTÁ ABAIXO DE 6.9' + normal)
    print(red + f'[!] - VOCÊ ESTÁ DE RECUPERAÇÃO' + normal)
elif media < 5:
    print(red + f'\n\n[!] - SUA MÉDIA FOI {media}, VOCÊ PASSOU POIS ESTÁ ACIMA DE 7.0' + normal)