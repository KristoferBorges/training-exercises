from modulo import Printador

print('=' * 6 + ' DESAFIO 76 ' + '=' * 6 + '\n\n')

produtos = (
    ("Lápis", 1.75), 
    ("Borracha", 2.0), 
    ("Caderno", 15.90), 
    ("Estojo", 25.00), 
    ("Transferidor", 4.20), 
    ("Compasso", 9.99), 
    ("Mochila", 120.32), 
    ("Canetas", 22.30),
    ("Livro", 34.90)
)

Printador.centralizador("LISTAGEM DE PREÇOS", "=", 40)
print("-" * 40)
for p, v in produtos:
    print("  {:.<30}R${:.2f}".format(p, v))
print("-" * 40)
    
