#Crie um programa que peça ao usuário o nome de um produto, em seguida crie um identificador único atrelado ao mesmo.
#Regras
#[ ! ] - Cada identificador precisa começar com 2 letras e terminar com 4 números;
#[ ! ] - Armazene todos os identificadores em um único arquivo no excel;
#[ ! ] - Não pode haver mais de um identificador único igual a outro;

#Extra: Crie uma opção de consultar os identificadores e produtos armazenados
import pandas as pd
import openpyxl
import random

def createID():
    """
    Função para criar um identificador único para um produto.
    """
    try:
        df_produtos = pd.read_excel('Hardcore/produtos.xlsx')

        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numeros = '0123456789'
        id = ''

        for letra in range(2):
            letra = random.choice(letras)
            id += letra
        
        for numero in range(4):
            numero = random.choice(numeros)
            id += numero
        
        # Processo de analise para verificar se o ID já existe
        for valor in df_produtos["ID"]:
            if id == valor:
                createID()
            else:
                print(f'\n[INFO]: Produto Cadastrado com Sucesso!')
                print(f'[INFO]: ID do Produto: {id}')
                return id
    
    except Exception as erro:
        print("\n[ERRO]: Algo impediu a criação do ID. Tente novamente.")
        print(f'[ERRO]: {erro}')

def salvarDados(produto, idProduto):
    """
    Função para salvar os dados do produto e seu identificador único.
    """
    try:
        df_produtos = pd.read_excel('Hardcore/produtos.xlsx')
        
        novosDados = {
            'ID' : idProduto,
            'PRODUTO' : produto,
        }

        df_produtos.loc[len(df_produtos)] = novosDados
        df_produtos.to_excel('Hardcore/produtos.xlsx', index=False)
    
    except Exception as erro:
        print(f'\n[ERRO]: {erro}')


def main():
    """
    Função principal do programa.
    """
    print('=' * 26 + ' DESAFIO HARD 05 ' + '=' * 26 + '\n\n')
    while True:
        print('\n[ 1 ] - Cadastrar Produto')
        print('[ 2 ] - Consultar Produtos')
        print('[ 3 ] - Sair')

        opcao = str(input('Opção: '))
        if opcao == '1':
            produto = str(input('\nNome do Produto: ')).strip()
            idProduto = createID()

            salvarDados(produto, idProduto)
        elif opcao == '2':
            try:
                df_produtos = pd.read_excel('Hardcore/produtos.xlsx')
                
                print('\n' + '=' * 26 + ' PRODUTOS CADASTRADOS ' + '=' * 26 + '\n')
                for id, produto in zip(df_produtos['ID'], df_produtos['PRODUTO']):
                    print(f'ID: {id} - Produto: {produto}')
                    

                print('\n' + '=' * 26 + ' FIM DA LISTA ' + '=' * 26 + '\n')

            except Exception as erro:
                print(f'\n[ERRO]: {erro}')
        elif opcao == '3':
            print('\n[INFO]: Encerrando o Programa...')
            break
        
        else:
            print('\n[ERRO]: Opção Inválida! Tente Novamente.')


if __name__ == '__main__':
    main()