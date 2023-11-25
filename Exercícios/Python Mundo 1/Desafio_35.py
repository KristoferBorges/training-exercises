# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
# podem ou não formar um triângulo.

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print('=' * 6 + ' DESAFIO 35 ' + '=' * 6)

reta1 = int(input(green + '\n\n[?] - RETA 1: '))
reta2 = int(input('[?] - RETA 2: '))
reta3 = int(input('[?] - RETA 3: '))

if (reta1 + reta2) > reta3:
    if (reta2 + reta3) > reta1:
        if (reta1 + reta3) > reta2:
            print(yellow + '\n[!] - COM BASE NAS RETAS, É POSSÍVEL FORMAR UM TRIÂNGULO!' + normal)
        else:
            print(red + '[!] - NÃO É POSSÍVEL FORMAR UM TRIÂNGULO' + normal)
else:
    print(red + '[!] - NÃO É POSSÍVEL FORMAR UM TRIÂNGULO' + normal)