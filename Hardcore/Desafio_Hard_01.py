import random
import time
numero = '200'

def encontrandoNumero(numero):
    print('[!] - COMEÇANDO A PROCURA EM 3 SEGUNDOS')
    time.sleep(1)
    print('[!] - COMEÇANDO A PROCURA EM 2 SEGUNDOS')
    time.sleep(1)
    print('[!] - COMEÇANDO A PROCURA EM 1 SEGUNDOS')
    time.sleep(1)

    tentativas = 0
    maxTentativas = 99999
    listaErrada = list()
    while True:
        numero1 = random.randint(0, 9)
        numero2 = random.randint(0, 9)
        numero3 = random.randint(0, 9)

        teste = numero[:0] + str(numero1) + numero[1:]
        teste = teste[:1] + str(numero2) + teste[2:]
        teste = teste[:2] + str(numero3) + teste[3:]


        while teste in listaErrada:
            numero1 = random.randint(0, 9)
            numero2 = random.randint(0, 9)
            numero3 = random.randint(0, 9)

            teste = numero[:0] + str(numero1) + numero[1:]
            teste = teste[:1] + str(numero2) + teste[2:]
            teste = teste[:2] + str(numero3) + teste[3:]
        
        print(f'\n[!] - TENTATIVA = [{tentativas}] - [{maxTentativas}]')
        print(f'[INFO] - {teste}')
        if tentativas == maxTentativas:
            print("\n[!] - NÚMERO NÃO ENCONTRADO")
            print('[!] - TENTATIVAS = [{maxTentativas}]')
            break
        elif teste == numero:
            print(f'\n[!] - NÚMERO ENCONTRADO = [{teste}]')
            print(f'[!] - TENTATIVAS FEITAS = [{tentativas}]')
            break
        else:
            listaErrada.append(teste)
        
        tentativas += 1


encontrandoNumero(numero)
while True:
    op = input("\n[?] - Deseja continuar? [S/N] ").upper()
    if op == 'S':
        numero = input("[?] - Digite um número: ")
        encontrandoNumero(numero)
    elif op == 'N':
        break