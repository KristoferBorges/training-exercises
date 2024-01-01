class Printador:
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    red = "\033[0;31m"
    normal = "\033[0m" # to come back to default

    def centralizador(titulo, caractere='=', largura_linha=80):
        espacos_laterais = (largura_linha - len(titulo) - 2) // 2
        linha = caractere * espacos_laterais + f' {titulo} ' + caractere * espacos_laterais
        return print('\n\n' + linha + '\n\n')
    