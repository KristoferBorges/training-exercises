# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 42 ' + '=' * 6)

reta1 = int(input(green + '\n\n[?] - RETA 1: '))
reta2 = int(input('[?] - RETA 2: '))
reta3 = int(input('[?] - RETA 3: '))

if (reta1 + reta2) > reta3:
    if (reta2 + reta3) > reta1:
        if (reta1 + reta3) > reta2:
            print(yellow + '\n[!] - COM BASE NAS RETAS, É POSSÍVEL FORMAR UM TRIÂNGULO!' + normal)
            
            # Analise do triângulo
            if reta1 == reta2 and reta1 == reta3:
                print(yellow + '[!] - TRIÂNGULO EQUILÁTERO' + normal)
            elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
                print(yellow + '[!] - TRIÂNGULO ISÓSCELES' + normal)
            elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
                print(yellow + '[!] - TRIÂNGULO ESCALENO' + normal)

        else:
            print(red + '[!] - NÃO É POSSÍVEL FORMAR UM TRIÂNGULO' + normal)
else:
    print(red + '[!] - NÃO É POSSÍVEL FORMAR UM TRIÂNGULO' + normal)
