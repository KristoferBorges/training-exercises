import random

numero = '99'

def encontrandoNumero(numero):
    tentativas = 0
    maxTentativas = 99999
    listaErrada = list()
    while True:
        numero1 = random.randint(0, 9)
        numero2 = random.randint(0, 9)

        teste = numero[0] + str(numero1) + numero[1]
        teste = numero[1] + str(numero2) + numero[2]

        while teste in listaErrada:
            numero1 = random.randint(0, 9)
            numero2 = random.randint(0, 9)

            teste = numero[0] + str(numero1) + numero[1]
            teste = numero[1] + str(numero2) + numero[2]
        
        if tentativas == maxTentativas:
            print("[!] - NÚMERO NÃO ENCONTRADO")
            print('[!] - TENTATIVAS = [{maxTentativas}]')
            break
        elif teste == numero:
            print(f'[!] - NÚMERO ENCONTRADO = [{teste}]')
            print(f'[!] - TENTATIVAS FEITAS = [{tentativas}]')
            break