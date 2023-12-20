from random import randint

print("=-" * 13)
print("VAMOS JOGAR ÍMPAR OU PAR")
print("=-" * 13)

computerValor = randint(1, 10)
computerChoice = ""
contVictory = 0

while (True):
    playerChoice = str(input("IMPAR OU PAR? [P/I]: ")[0].upper())
    if playerChoice != "P" and playerChoice != "I":
        print('[AVISO] - INFORME APENAS [P/I]')
        playerChoice = str(input("IMPAR OU PAR? [P/I]: ")[0].upper())
        if playerChoice != "P" and playerChoice != "I":
            break

    playerValor = int(input("Escolha um número para jogar: "))

    if playerChoice == "P":
        computerChoice = "I"
    else:
        computerChoice = "P"

    if (playerValor + computerValor) % 2 == 0:
        if playerChoice == "P":
            print("\nUSUÁRIO WIN")
            print(f"\nVALOR FINAL [{playerValor + computerValor}] = PAR")
            contVictory += 1
        else:
            print("\nCOMPUTADOR WIN")
            print(f"\nVALOR FINAL [{playerValor + computerValor}] = PAR")
            break
    else:
        if playerChoice == "I":
            print("\nUSUÁRIO WIN")
            print(f"\nVALOR FINAL [{playerValor + computerValor}] = ÍMPAR")
            contVictory += 1
        else:
            print("\nCOMPUTADOR WIN")
            print(f"\nVALOR FINAL [{playerValor + computerValor}] = ÍMPAR")
            break

print(f"\n\n QUANTIDADE DE VITÓRIAS [{contVictory}]")