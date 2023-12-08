# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('[?] - Informe o salário do funcionário: R$'))
novoSalario = salario + (salario * 15 / 100)

print(f'[!] - O salário do funcionário é de R${salario:.2f}, porém, com o nosso aumento de [15%] o valor final fica de R${novoSalario:.2f}')