import Funcoes

def OptionOne():
    try:
        arq = open('cadastros.txt', 'r')
    except:
        print('Não foi possivel abrir o arquivo')
    else:
        for linha in arq:
            dado = linha.split(';')
            dado[1].replace('\n', '')
            print(f'Nome: {dado[0]}, Idade: {dado[1]}', end='')
    finally:
        arq.close()
        


def OptionTwo():
    with open('cadastros.txt', 'a') as arq:
        pessoa = {'Nome':'', 'Idade': ''}
        pessoa['Nome'] = str(input('Nome: '))
        pessoa['Idade'] = Funcoes.leiaInt()
        arq.write(f'{pessoa["Nome"]};{pessoa["Idade"]}\n')
