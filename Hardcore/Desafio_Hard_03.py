# Desenvolver um script para gerar códigos promocionais, o código também terá um verificador de código para saber se o código informado é válido.

import os
import subprocess
import datetime
import random
import string
import pandas as pd
import openpyxl
from time import sleep

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
black = "\033[0;30m"
white = "\033[0;37m"
blue = "\033[0;34m"
cyan = "\033[0;36m"
purple = "\033[0;35m"
light_gray = "\033[0;37m"
dark_gray = "\033[1;30m"
normal = "\033[0m" # to come back to default 

caminhoArquivoCodigos = 'Hardcore/codigos.xlsx'

def centralizar_titulo(titulo, caractere='='):
    largura_linha = 80 
    espacos_laterais = (largura_linha - len(titulo) - 2) // 2
    linha = caractere * espacos_laterais + f' {titulo} ' + caractere * espacos_laterais
    return print('\n\n' + linha + '\n\n')


def salvamentoExcel(codigo, vencimento):
    # Lendo os dados
    try:
        df_antigo = pd.read_excel(caminhoArquivoCodigos)
    except FileNotFoundError:
        df_antigo = pd.DataFrame()

    # Criação dos dados
    dados = {
        'Codigo': [codigo],
        'Vencimento': [vencimento]
    }

    # Novo DataFrame
    df_novo = pd.DataFrame(dados)

    # Junta os dois DataFrames
    df_final = pd.concat([df_antigo, df_novo], ignore_index=True)

    # Salvamento dos dados
    df_final.to_excel(caminhoArquivoCodigos, index=False)


def gerarCodigo(desconto, tempo):

    # Geração de código
    letras = string.ascii_letters
    baseCodigo = ''.join(random.choice(letras) for _ in range(1, 7 + 1))
    codigo = baseCodigo + f'{desconto}'
    dataAtual = datetime.datetime.now()
    dataVencimento = dataAtual + datetime.timedelta(days=tempo)
    dataVencimento = dataVencimento.strftime("%d-%m-%Y")

    # Função para salvar os dados
    salvamentoExcel(codigo, dataVencimento)
    # Retorno do codigo pronto
    return codigo, dataVencimento


def verificaCodigo(codigo):
    df_arquivo = pd.read_excel(caminhoArquivoCodigos)
    procurarCodigo = codigo
    dataAtual = datetime.datetime.now()

    filtro = df_arquivo['Codigo'].str.contains(procurarCodigo)
    encontrado = df_arquivo[filtro]

    if not encontrado.empty:
        print(green + f'\n\t[ ! ] - O CÓDIGO ENCONTRADO.' + normal)
        centralizar_titulo('CÓDIGOS')

        codigo = encontrado['Codigo'].iloc[0]
        dataVencimento_str = encontrado['Vencimento'].iloc[0]
        
        # Convertendo a string para objeto datetime com o formato %d/%m/%Y
        dataVencimento = datetime.datetime.strptime(dataVencimento_str, "%d-%m-%Y")

        # Comparação apenas das partes da data
        if dataAtual.date() > dataVencimento.date():
            status = red + 'DESATIVADO' + normal
        elif dataAtual.date() < dataVencimento.date():
            status = green + 'ATIVO' + normal
        else:
            status = green + 'HOJE/ATIVO' + normal

        print(cyan + f'\n\t[ # ] - CÓDIGO: ' + purple + f'{codigo}' + normal + ' | ' + cyan + 'VENCIMENTO: ' + purple + f'{dataVencimento_str}' + normal)
        print(cyan + f'\t[ INFO ] - STATUS: {status}' + normal)
    else:
        print(red + f'\n\t[ ! ] - O CÓDIGO NÃO FOI ENCONTRADO.' + normal)


def consultarPasta():
    caminhoArquivo = caminhoArquivoCodigos

    if os.path.exists(caminhoArquivo):
        subprocess.Popen(['start', 'excel', caminhoArquivo], shell=True)
    else:
        print(f'O arquivo {caminhoArquivo} não existe.')

def main():
    while True:
        centralizar_titulo('ADMINISTRADOR DE CÓDIGOS')
        print(yellow + '\t[ 1 ]' + normal + ' - ' + green + 'GERAR CÓDIGOS' + normal)
        print(yellow + '\t[ 2 ]' + normal + ' - ' + green + 'AUTENTICAR CÓDIGO' + normal)
        print(yellow + '\t[ 3 ]' + normal + ' - ' + green + 'CONSULTAR PASTA DE CÓDIGOS' + normal)
        print(yellow + '\t[ 4 ]' + normal + ' - ' + red + 'SAIR DO PROGRAMA' + normal)

        op = str(input('\t[ ? ] - INFORME SUA ESCOLHA: '))
        if op == '1':
            centralizar_titulo('GERADOR DE CÓDIGOS')
            desconto = int(input(yellow + '\t[ ? ] - INFORME O VALOR EM [%] PARA DESCONTO: ' + normal))
            tempo = int(input(yellow + '\t[ ? ] - INFORME O TEMPO EM [DIA(S)] PARA O VENCIMENTO: ' + normal))
            quantidade = int(input(yellow + '\t[ ? ] - INFORME A QUANTIDADE EM [UNIDADES] PARA GERAR: ' + normal))

            for i in range(1, quantidade + 1):
                codigo, dataVencimento = gerarCodigo(desconto, tempo)
                sleep(0.3)
                print(green + '\n\t[ ! ] - GERANDO CÓDIGO.' + normal)
                sleep(0.2)
                print(green + '\t[ ! ] - GERANDO CÓDIGO..' + normal)
                sleep(0.1)
                print(green + '\t[ ! ] - GERANDO CÓDIGO...' + normal)
                sleep(0.1)
                print(yellow + f'\n\t[ {i}º ] - [CODIGO: {codigo}] | [VENCIMENTO: {dataVencimento}]' + normal)

        elif op == '2':
            centralizar_titulo('AUTENTICADOR DE CÓDIGOS')
            codigo = str(input(yellow + '\n\t[ ? ] - INFORME O CÓDIGO PARA VERIFICAR: ' + normal))
            verificaCodigo(codigo)

        elif op == '3':
            consultarPasta()

        elif op == '4':
            print(green + '\n\t[ ! ] - OBRIGADO POR UTILIZAR NOSSO SOFTWARE.' + normal)
            break
        else:
            print(red + '\n\t[ ! ] - OPÇÃO INVÁLIDA.' + normal)


if __name__ == '__main__':
    main()

