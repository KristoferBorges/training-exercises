# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.                                                                                                              
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
PessoasMenorPeso = list()
PessoasMaiorPeso = list()
contPessoas= 0
maiorPeso= 0
menorPeso= 0
nomeMaiorPeso = ''
nomeMenorPeso = ''
print(' ----------+ CADASTRO +----------')
while True:
    pessoa = str(input(' Nome: '))
    peso = int(input(' Peso: '))
    pessoas.append(pessoa)
    pessoas.append(peso)
    
    if contPessoas == 0:
        maiorPeso = peso
        menorPeso = peso
    elif contPessoas > 0:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso
    contPessoas += 1

    saida = input(' Deseja continuar? [ S/N ]: ').upper()
    if saida == 'N':
        break 

for p in range(0, len(pessoas), 2):
    if maiorPeso == pessoas[p+1]:
        PessoasMaiorPeso.append(pessoas[p])
        PessoasMaiorPeso.append(pessoas[p+1])
    elif menorPeso == pessoas[p+1]:
        PessoasMenorPeso.append(pessoas[p])
        PessoasMenorPeso.append(pessoas[p+1])
    else:
        pass


print(f' Ao todo, você cadastrou {contPessoas} pessoas.')
print(f' O maior peso foi de {maiorPeso}.0Kg. Peso de ', end='')
for pessoa in range(0, len(PessoasMaiorPeso)):
    if pessoa % 2 == 0:
        print(f'[{PessoasMaiorPeso[pessoa]}]', end=' ')

print(f'\n O menor peso foi de {menorPeso}.0Kg. Peso de ', end='')
for pessoa in range(0, len(PessoasMenorPeso)):
    if pessoa % 2 == 0:
        print(f'[{PessoasMenorPeso[pessoa]}]', end=' ')
print("\n")