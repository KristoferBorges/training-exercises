from modulo import Printador

print('=' * 6 + ' DESAFIO 77 ' + '=' * 6 + '\n\n')

palavras = (
    "APRENDER", 
    "PROGRAMAR", 
    "LINGUAGEM", 
    "PYTHON", 
    "CURSO", 
    "GRATIS", 
    "ESTUDAR", 
    "PRATICAR", 
    "TRABALHAR", 
    "MERCADO", 
    "PROGRAMADOR", 
    "FUTURO"
)

for palavra in palavras:
    print(f"Na palavra {palavra} temos: ", end=" ")
    for i in range(0, len(palavra)):
        if palavra[i] == "A":
            print("a", end=" ")
        if palavra[i] == "E":
            print("e", end=" ")
        if palavra[i] == "I":
            print("i", end=" ")
        if palavra[i] == "O":
            print("o", end=" ")
        if palavra[i] == "U":
            print("u", end=" ")
    print("")
