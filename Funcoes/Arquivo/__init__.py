def OptionOne():
    arq = open('cadastros.txt', 'r')
    for valor in arq:
        print(valor, end='')


def OptionTwo():
    with open('cadastros.txt', 'a') as arq:
        pessoa = {'Nome':'', 'Idade': ''}
        pessoa['Nome'] = str(input('Nome: '))
        pessoa['Idade'] = str(input('Idade: '))
        arq.write(f'Nome: {pessoa["Nome"]} \n')
        arq.write(f'Idade: {pessoa["Idade"]}\n')
