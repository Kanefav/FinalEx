import Funcoes as func

if func.ArquivoExist('cadastros.txt') == True:
    print('arquivo carregado com sucesso')
    func.menu()
else:
    print('arquivo não carregado')
    func.CriarArquivo('cadastros.txt')
    print('tente executar novamente')
    