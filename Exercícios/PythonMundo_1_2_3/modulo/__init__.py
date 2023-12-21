class Printador:
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    red = "\033[0;31m"
    normal = "\033[0m" # to come back to default

    def centralizador(texto):
        largura_terminal = 50  # Substitua pelo valor adequado à largura do seu terminal

        espacos_esquerda = (largura_terminal - len(texto)) // 2
        espacos_direita = largura_terminal - len(texto) - espacos_esquerda

        linha_centralizada = f"{' ' * espacos_esquerda}{texto}{' ' * espacos_direita}"
        print("=-" * 18)
        print(linha_centralizada)
        print("=-" * 18)