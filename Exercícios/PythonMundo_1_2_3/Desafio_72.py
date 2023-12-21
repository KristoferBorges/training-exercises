from modulo import Printador

def numerosPorExtenso(number):
    numeros = tuple(["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"])

    while True:
        try:
            number = int(number)

            if number > 20 or number < 0:
                print(Printador.green + "[!] - APENAS NÚMEROS DE 0 A 20" + Printador.normal)
                number = int(input("INFORME UM NÚMERO: "))
            else:
                print(f"VOCÊ DIGITOU O NÚMERO [{numeros[number]}]")
                break
        except ValueError:
            print("[!] - O VALOR NÃO PODE SER DIFERENTE DE UM NÚMERO")
            number = int(input("INFORME UM NÚMERO: "))
            continue
        except Exception as error:
            print("[!] - APENAS NÚMEROS DE 0 A 20")
            print(error)
            number = int(input("INFORME UM NÚMERO: "))
        
            
   

numberInput = input(Printador.green + "INFORME UM NÚMERO: " + Printador.normal)
numerosPorExtenso(numberInput)