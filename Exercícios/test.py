def analisaIdade(idade):
    if idade >= 18 and idade <= 23:
        return True
    else:
        return False

resultado = analisaIdade(22)
print(resultado)