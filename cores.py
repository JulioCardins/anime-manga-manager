def vermelho(msg):
    return f"\033[31m{msg}\033[m"
def azul(msg):
    return f"\033[1;34m{msg}\033[m"
def amarelo(msg):
    return f"\033[1;33m{msg}\033[m"
def verde(msg):
    return f"\033[1;32m{msg}\033[m"
def branco(msg):
    return f"\033[1;97m{msg}\033[m"
def preto(msg):
    return f"\033[1;30m{msg}\033[m"

'''obras = list()
    try:
        with open("animes.txt", mode="r", encoding="utf-8") as arquivo:
            cabecalho("ESCOLHA A OBRA PARA EXCLUIR")
            c = 1
            for item in arquivo:
                dado = item.strip().split(";")
                obra = {"nome": dado[0],
                "nota": int(dado[1]),
                "status": dado[2] == "True",
                "categoria": dado[3],
                "interesse": dado[4] == "True",
                "analise": dado[5].strip()
                }
                obras.append(obra)
                if obra['interesse']:
                    print(f"{amarelo(f"[{c}]")} {azul(obra["nome"])} | {azul(obra["categoria"])} | {azul('Lista de interesse')}")
                else:
                    print(f"{amarelo(f"[{c}]")} {azul(obra["nome"])} | {azul(obra["categoria"])}")
                c += 1
            if len(obras) == 0:
                print(vermelho("NENHUMA OBRA CADASTRADA!"))
                return
            escolha = validarEscolha(input("Sua escolha: "), len(obras)) - 1
            print(f"{branco("Você escolheu excluir o item")} {azul(obras[escolha]['nome'])} | {azul(obras[escolha]['categoria'])}")
            print(f"{branco("TEM CERTEZA QUE DESEJA EXCLUIR? A AÇÃO NÃO PODERÁ SER DESFEITA!!")}")
            print(f"{amarelo("[1]")} - {vermelho("EXCLUIR")}      {amarelo("[2]")} - {verde("VOLTAR")}")
            opcao = validarEscolha(input("Sua opção: "))
            match opcao:
                case 1:
                    print(verde("Processando..."))
                    sleep(1)
                    nome_excluido = obras[escolha]['nome']
                    categoria_excluido = obras[escolha]['categoria']
                    obras.pop(escolha)
                    try:
                        with open("animes.txt", mode="w", encoding="utf-8") as arquivo:
                            for obra in obras:
                                obra_formatada = f"{obra['nome']};{obra['nota']};{obra['status']};{obra['categoria']};{obra['interesse']};{obra['analise']}\n"
                                arquivo.write(obra_formatada)
                    except PermissionError:
                        print(vermelho("ERRO: SEM PERMISSÃO PARA ESCREVER NO ARQUIVO."))
                    except OSError:
                        print(vermelho("ERRO: OCORREU UM PROBLEMA AO ACESSAR O ARQUIVO."))
                    else:
                        print(verde(f"OBRA {azul(nome_excluido)} | {azul(categoria_excluido)} {verde("DELETADA COM SUCESSO!")}"))
                        sleep(1)
                case 2:
                    print(verde("Retornando ao menu..."))
                    sleep(1)
                    return
    except FileNotFoundError:
        print(vermelho("ERRO, ARQUIVO NÃO ENCONTRADO!"))
    except IndexError:
        print(vermelho("ERRO DE ÍNDICE"))'''

'''            try:
                with open("animes.txt", mode="w", encoding="utf-8") as arquivo:
                    for obra in obras:
                        obra_formatada = f"{obra['nome']};{obra['nota']};{obra['status']};{obra['categoria']};{obra['interesse']};{obra['analise']}\n"
                        arquivo.write(obra_formatada)
            except PermissionError:
                print(vermelho("ERRO: SEM PERMISSÃO PARA ESCREVER NO ARQUIVO."))
            except OSError:
                print(vermelho("ERRO: OCORREU UM PROBLEMA AO ACESSAR O ARQUIVO."))
            else:
                print(verde(f"OBRA {azul(nome_excluido)} | {azul(categoria_excluido)} {verde("DELETADA COM SUCESSO!")}"))
                sleep(1)'''