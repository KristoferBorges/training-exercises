from modulo import Printador

numeros = tuple()
text = ""

n1 = int(input("\nDIGITE O PRIMEIRO NÚMERO: "))
n2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
n3 = int(input("DIGITE O TERCEIRO NÚMERO: "))
n4 = int(input("DIGITE O QUARTO NÚMERO: "))

numeros = (n1, n2, n3, n4)

if 3 in numeros:
    number_3 = numeros.index(3) + 1
    text = f"O VALOR [3] APARECEU PELA PRIMEIRA VEZ NA POSIÇÃO [{number_3}º]"
else:
    text = "O VALOR [3] NÃO APARECEU EM NENHUMA POSIÇÃO!"


print(f"\nVOCÊ DIGITOU OS NUMEROS: {numeros}")
print(f"O VALOR [9] FOI DIGITADO [{numeros.count(9)}] VEZES")
print(text)
print(f"OS VALORES PARES DIGITADOS FORAM: ", end= "")

for num in numeros:
    if num % 2 == 0:
        print(f"{num}",end= " ")
    else:
        pass
print("FIM")
