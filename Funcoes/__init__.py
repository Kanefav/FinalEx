from Funcoes.Arquivo import OptionTwo
from Funcoes import Arquivo


def menu():
    while True:
        try: 
            print('--'*14)
            print('       Menu Principal')
            print('--'*14)
            print('''1 - Ver pessoas cadastradas
2 - Cadastras nova pessoa
3 - Sair do Sistema''')
            print('--'*14)        
            option = int(input('Sua opção: '))
            if option == 1:
                Arquivo.OptionOne()
            if option == 2:
                Arquivo.OptionTwo()
            if option == 3:
                print('Saindo do Sistema')
                print('--'*14)  
                break
        except ValueError:
            print('Erro, digite uma opção valida')
        except Exception as erro:
            print(f'Ocorreu um erro desconhecido, relatório de erro: {erro}')


def ArquivoExist(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except Exception as erro:
        print(f'Erro na criação do arquivo, relatório de erro: {erro}')
    else:
        print('arquivo criado com sucesso')