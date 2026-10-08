from cores import *
from funcoes import *
from time import sleep
from banco import criarBanco

criarBanco()
if arquivoExiste("animes.txt"):
    while True:
        escolha = menu(["Adicionar Obra", "Mostrar Obras Cadastradas", "Editar Obras Cadastradas", "Excluir Obras Cadastradas", "Importar Obras", "Exportar Obras" ,"Sair do Sistema"])
        match escolha:
            case 1:
                print(verde("Processando..."))
                sleep(1)
                cadastrar()
            case 2:
                print(verde("Processando..."))
                sleep(1)
                listar()
            case 3:
                print(verde("Processando..."))
                sleep(1)
                editar()
            case 4:
                print(verde("Processando..."))
                sleep(1)
                deletar()
            case 5:
                print(verde("Processando..."))
                sleep(1)
                importarObras()
            case 6:
                print(verde("Processando..."))
                sleep(1)
                exportarObras()
            case 7:
                print(verde("Processando..."))
                sleep(1)
                print(verde("PROGRAMA ENCERRADO COM SUCESSO, ATÉ LOGO!!!"))
                break
else:
    print(vermelho("O ARQUIVO PARA CADASTRO NÃO EXISTE! FAVOR CRIAR"))
