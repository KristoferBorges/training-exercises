mais18 = 0
qntHomens = 0
mulheresMenos20 = 0


while (True):
    print("\tCADASTRO DE PESSOAS")

    idade = int(input('QUANTOS ANOS: '))
    sexo = str(input('SEXO [M / F]: ').strip().upper()[0])

    if sexo == "M":
        qntHomens += 1

    if idade >= 18:
        mais18 += 1

    if sexo == "F":
        if idade < 20:
            mulheresMenos20 += 1
    
    escolha = str(input("PESSOA CADASTRADA COM SUCESSO, DESEJA CONTINUAR ? [S/N]").upper()[0])
    if escolha == "S":
        continue
    else:
        break

print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS = [{mais18}]')
print(f'AO TODO TEMOS [{qntHomens}] CADASTRADOS')
print(f'E TEMOS [{mulheresMenos20}]')
    