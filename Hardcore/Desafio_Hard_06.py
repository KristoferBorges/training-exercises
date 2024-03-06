# Desafio não finalizado

def criadorDePiramide(tamanho):
    print("\n")
    espaco = tamanho
    caractere = "*"
    for i in range(0, tamanho):
        if espaco != 0:
            print(f' ' * (espaco), end="")
            espaco -= 1
        if i == 0:
            print(f'{caractere}' * (i+1))
        elif i == 1:
            print(f'{caractere}' * (i+2))
        else:
            print(f'{caractere}' * (i+3))

tamanho_input = int(input("Qual o tamanho da pirâmide?\n--> "))
criadorDePiramide(tamanho_input)