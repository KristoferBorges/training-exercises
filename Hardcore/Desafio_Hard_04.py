#Faça um programa que pegue informações do usuário, e identifique se ele(a) é legível com base na análise, 
#apresente a informação no terminal sobre o status dessa análise:
#Informações para Coleta
#@ Nome completo;
#@ Idade;
#@ CPF;
#@ Telefone;

#Informações para Analisar
#@ Nome completo (Não pode haver números);
#@ Idade (Precisa ser maior que 18 anos e menor que 23 anos);
#@ CPF (EX: 237.832.53(8)-02) - O terceiro último número precisa ser 8;
#@ Telefone (O DDD do número precisa ser 11);

#Contexto: Uma empresa de tecnologia está procurando jovens do estado de São Paulo para oferecerem vagas de Jovem aprendiz,
#isso precisamos analisar os dados inseridos por eles e identificar se são legíveis ao processo de Jovem aprendiz.

def analisaNome(nome):
    nome = nome.strip()
    if nome.isalpha() or ' ' in nome:
        return True
    else:
        return False
    
def analisaIdade(idade):
    if idade >= 18 and idade <= 23:
        return True
    else:
        return False
    
def analisaCPF(cpf):
    cpf = cpf.replace('.' or '-', '')
    if len(cpf) == 11 and cpf[8] == '8':
        return True
    else:
        return False

def analisaTelefone(telefone):
    telefone = telefone.replace('-', '')
    if len(telefone) == 11 and telefone[:2] == '11':
        return True
    else:
        return False

def main():
    try:
        print('=' * 26 + ' DESAFIO HARD 04 ' + '=' * 26 + '\n\n')
        nomeCompleto = str(input('\tNome Completo: '))
        resultNome = analisaNome(nomeCompleto)
        
        idade = int(input('\tIdade: '))
        resultIdade = analisaIdade(idade)

        cpf = str(input('\tCPF: '))
        resultCPF = analisaCPF(cpf)

        telefone = str(input('\tTelefone: '))
        resultTelefone = analisaTelefone(telefone)

        print('\n\n' + '=' * 26 + ' RESULTADO ' + '=' * 26 + '\n')
        print(f'\tNome: {resultNome}')
        print(f'\tIdade: {resultIdade}')
        print(f'\tCPF: {resultCPF}')
        print(f'\tTelefone: {resultTelefone}')

        if resultNome and resultIdade and resultCPF and resultTelefone:
            print('\n\n\t[!] - Parabéns, você é legível ao processo de Jovem Aprendiz!\n')
        else:
            print('\n\n\t[!] - Infelizmente, você não é legível ao processo de Jovem Aprendiz!\n')

    except Exception as error:
        print(f'Erro: {error}')

if __name__ == '__main__':
    main()