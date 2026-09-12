import math
from time import sleep
from cores import *
import json

def linha(tamanho=50):
    """
    :param tamanho: Tamanho da linha pré definida
    :return: Retorna a linha com o tamanho já definido
    """
    return '~'*tamanho
def cabecalho(msg):
    """
    :param msg: Retorna a mensagem já formatada com as linhas
    :return:
    """
    print(branco(linha()))
    print(branco(msg).center(55))
    print(branco(linha()))
def menu(opcoes):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in opcoes:
        print(f"{amarelo(c)} - {azul(item)}")
        c += 1
    print(linha())
    opc = validarEscolha(input("Sua opção: "), len(opcoes))
    return opc
def notas():
    print(linha())
    print("""[10] - OBRA PRIMA 🤩
[9] - ÓTIMO 😍
[8] - MUITO BOM 😎
[7] - BOM 😁
[6] - LEGAL 🙂
[5] - ATÉ VAI 😐
[4] - RUIM 😬
[3] - MUITO RUIM 😒
[2] - LIXO 🫩
[1] - HORRÍVEL 💀""")
    print(linha())
def concluidoOpcao():
    print(linha())
    print("""Obra concluida? 
[1] - SIM
[2] - NÃO, em andamento""")
def validarNota(nota):
    """
    :param nota: recebe uma nota do usuário, e trata o valor recebido para garantir que o valor seja válido
    :return: retorna a nota formatada como um valor inteiro
    """
    while True:
        nota = nota.strip()
        if nota.isnumeric():
            nota = int(nota)
            if nota >= 1 and nota <= 10:
                return nota
            else:
                nota = input(vermelho('Por favor, digite uma nota valida: '))
        else:
            nota = input(vermelho('Por favor, digite uma nota valida: '))
def validarEscolha(escolha, tamanho=2):
    """
    :param escolha: recebe o numero fornecido pelo usuário, verifica se é númerico e passa para inteiro
    :param tamanho: recebe o tamanho das opções para validação
    :return: retorna o valor já convertido para inteiro no intervalo válido
    """
    while True:
        escolha = escolha.strip()
        if escolha.isnumeric():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= tamanho:
                return escolha
            else:
                escolha = input(vermelho('Por favor, digite uma opção valida: '))
        else:
            escolha = input(vermelho('Por favor, digite uma opção valida: '))
def validarNome(nome):
    while True:
        nome = nome.strip()
        if nome == "":
            nome = input(vermelho("Por favor, digite um nome válido:"))
        else:
            return nome
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def mostrarObrasSelecao(obras):
    c = 1
    for obra in obras:
        if obra["interesse"]:
            print(
                f"{amarelo(f"[{c}]")} {azul(obra["nome"])} | {azul(obra["categoria"])} | {azul('Lista de Interesse')}")
        else:
            print(f"{amarelo(f"[{c}]")} {azul(obra["nome"])} | {azul(obra["categoria"])}")
        c += 1
def carregarObras():
    obras = list()
    try:
        with open("animes.txt", mode="r", encoding="utf-8") as arquivo:
            for item in arquivo:
                dado = item.strip().split(";", 5)
                obra = {"nome": dado[0],
                        "nota": int(dado[1]),
                        "status": dado[2] == "True",
                        "categoria": dado[3],
                        "interesse": dado[4] == "True",
                        "analise": dado[5].strip()
                        }
                obras.append(obra)
    except ValueError:
        print(vermelho("ERRO: DADOS INVÁLIDOS NO ARQUIVO!"))
        return
    except FileNotFoundError:
        return []
    except IndexError:
        print(vermelho("ARQUIVO COM FORMATO INVÁLIDO"))
        return
    else:
        return obras
def salvarObras(obras):
    try:
        with open("animes.txt", mode="w", encoding="utf-8") as arquivo:
            for obra in obras:
                obra_formatada = f"{obra['nome']};{obra['nota']};{obra['status']};{obra['categoria']};{obra['interesse']};{obra['analise']}\n"
                arquivo.write(obra_formatada)
    except PermissionError:
        print(vermelho("ERRO: SEM PERMISSÃO PARA ESCREVER NO ARQUIVO."))
        return False
    except OSError:
        print(vermelho("ERRO: OCORREU UM PROBLEMA AO ACESSAR O ARQUIVO."))
        return False
    else:
       return True
def cadastrar():
    """
   
    :return:
    """
    obras = carregarObras()
    if obras is None:
        return
    while True:
        nome = validarNome(input(f"{branco("Digite o nome da obra: ")} "))
        print(branco("Qual a categoria da obra? "))
        print(branco("[1] - Anime [2] - Mangá"))
        categoria = validarEscolha(input("Sua opção: "))
        match categoria:
            case 1:
                categoria = "Anime"
            case 2:
                categoria = "Manga"
        print(branco("Como deseja adicionar a obra? "))
        print(branco("[1] - Lista de Interesses [2] - Já Comecei"))
        tipo_cadastro = validarEscolha(input("Sua opção: "))
        match tipo_cadastro:
            case 1:
                nota = 0
                concluido = False
                interesse = True
                analise = "<SEM ANALISE>"
            case 2:
                print(branco("O que achou da obra? "))
                notas()
                nota = validarNota(input("Sua opção: "))
                concluidoOpcao()
                concluido = validarEscolha(input("Sua opção: "))
                match concluido:
                    case 1:
                        concluido = True
                    case 2:
                        concluido = False
                interesse = False
                print(branco("Deseja adicionar uma breve analise da obra? "))
                print(branco("[1] - SIM [2] - Não"))
                opc = validarEscolha(input("Sua Opção: "))

                if opc == 1:
                    analise = input("Digite sua analise da obra: ")
                    if analise.strip() == "":
                        analise = "<SEM ANALISE>"
                else:
                    analise = "<SEM ANALISE>"
        apresentacao ={'nome': nome,
            'nota': nota,
            'status': concluido,
            'categoria': categoria,
            'interesse': interesse,
            'analise': analise,
        }
        obras.append(apresentacao)
        if salvarObras(obras):
            print("UM MOMENTO...")
            sleep(1)
            print(verde("OBRA CADASTRADA COM SUCESSO!"))
            sleep(1)
            print(branco("Deseja adicionar uma outra obra?"))
            print(branco("[1] - SIM [2] - Não"))
            op = validarEscolha(input("Sua opção: "))
            if op == 1:
                continue
            else:
                return
        else:
            print(vermelho('NÃO FOI POSSÍVEL ADICIONAR A NOVA OBRA'))
            return
def listar():
    obras_interesses = list()
    obras_consumidas = list()
    inicio = 0
    itens_por_pagina = 5
    fim = itens_por_pagina
    pagina = 1
    cabecalho("OBRAS CADASTRADAS")
    obras = carregarObras()
    if obras is None:
        return
    if len(obras) == 0:
        print(vermelho("NENHUMA OBRA CADASTRADA!"))
        return
    for obra in obras:
        if obra["interesse"]:
            obras_interesses.append(obra)
        else:
            obras_consumidas.append(obra)
    print(branco('COMO DESEJA VER SUAS OBRAS? '))
    print(branco("[1] - CONSUMIDAS [2] - LISTA DE INTERESSE"))
    opc = validarEscolha(input("Sua opção: "))
    if opc == 1:
        lista_atual = obras_consumidas
        titulo = 'CONSUMIDOS'
    else:
        lista_atual =obras_interesses
        titulo = 'LISTA DE INTERESSE'
    if len(lista_atual) == 0:
        print(vermelho('SEM OBRAS CADASTRADAS!'))
        return
    tot_paginas = math.ceil(len(lista_atual) / itens_por_pagina)
    while True:
        cabecalho(titulo)
        if opc == 1:
            for obra in lista_atual[inicio:fim]:
                match obra["nota"]:
                    case 1:
                        nota_apresentada = vermelho("[1] - HORRÍVEL")
                    case 2:
                        nota_apresentada = vermelho("[2] - LIXO")
                    case 3:
                        nota_apresentada = vermelho("[3] - MUITO RUIM")
                    case 4:
                        nota_apresentada = vermelho("[4] - RUIM")
                    case 5:
                        nota_apresentada = vermelho("[5] - ATÉ VAI")
                    case 6:
                        nota_apresentada = verde("[6] - LEGAL")
                    case 7:
                        nota_apresentada = verde("[7] - BOM")
                    case 8:
                        nota_apresentada = verde("[8] - MUITO BOM")
                    case 9:
                        nota_apresentada = verde("[9] - ÓTIMO")
                    case 10:
                        nota_apresentada = verde("[10] - OBRA PRIMA")
                    case _:
                        nota_apresentada = "Nota Invalida"
                if obra["status"]:
                    status_apresentado = amarelo("Concluido")
                else:
                    status_apresentado = amarelo("Em andamento")
                print(linha())
                print(f"{branco('Nome:')} {azul(obra['nome'])}")
                print(f"{branco('Categoria:')} {azul(obra['categoria'])}")
                print(f"{branco('Nota:')} {nota_apresentada}")
                print(f"{branco('Status:')} {status_apresentado}")
                print(f"{branco('Análise:')}")
                print(obra['analise'])
                print(linha())
        else:
            for obra in lista_atual[inicio:fim]:
                print(linha())
                print(f"{branco('Nome:')} {azul(obra['nome'])}")
                print(f"{branco('Categoria:')} {azul(obra['categoria'])}")
                print(linha())

        print(azul(f"Página {pagina} de {tot_paginas}"))
        print(linha())
        print(f"{amarelo(f"[1]")} {verde("PRÓXIMO")}")
        print(f"{amarelo(f"[2]")} {verde("ANTERIOR")}")
        print(f"{amarelo(f"[3]")} {vermelho("VOLTAR")}")
        escolha = validarEscolha(input("Sua Opção: "),3)
        match escolha:
            case 1:
                if fim >= len(lista_atual):
                    print(f"{vermelho("NÃO HÁ PRÓXIMA PÁGINA")}")
                    continue
                inicio += itens_por_pagina
                fim += itens_por_pagina
                pagina += 1
            case 2:
                if inicio == 0:
                    print(f"{vermelho("NÃO HÁ PÁGINA ANTERIOR")}")
                    continue
                inicio -= itens_por_pagina
                fim -= itens_por_pagina
                pagina -= 1
            case 3:
                return


def editar():
    msg = vermelho("PARA ALTERNAR VALORES DE OBRAS NA LISTA DE INTERESSE, POR FAVOR, SELECIONE A OPÇÃO --- INTERESSE --- EM EDITAR OBRAS")
    obras = carregarObras()
    if obras is None:
        return
    if len(obras) == 0:
        print(vermelho("NENHUMA OBRA CADASTRADA!"))
        return
    mostrarObrasSelecao(obras)
    escolha = validarEscolha(input("Sua escolha: "), len(obras)) - 1
    obra_escolhida = obras[escolha]
    print(f"{branco("Você escolheu editar a obra: ")} {azul(obra_escolhida["nome"])}")
    print(branco("O que vamos editar? "))
    print(f"{amarelo("[1]")} {azul("Nome: ")}")
    print(f"{amarelo("[2]")} {azul("Nota: ")}")
    print(f"{amarelo("[3]")} {azul("Status de conclusão:")}")
    print(f"{amarelo("[4]")} {azul("Categoria: ")}")
    print(f"{amarelo("[5]")} {azul("Interesse: ")}")
    print(f"{amarelo("[6]")} {azul("Analise: ")}")
    print(f"{amarelo("[7]")} {azul("Voltar")}")
    escolha_editar = validarEscolha(input("Sua escolha: "), 7)
    match escolha_editar:
        case 1:
            novo_nome = validarNome(input("Digite o nome atualizado: "))
            obra_escolhida["nome"] = novo_nome
        case 2:
            if obra_escolhida['interesse']:
                print(msg)
                return
            nova_nota = validarNota(input("Digite a nota atualizada: "))
            obra_escolhida["nota"] = nova_nota
        case 3:
            if obra_escolhida['interesse']:
                print(msg)
                return
            concluidoOpcao()
            novo_status = validarEscolha(input("Sua opção: "))
            match novo_status:
                case 1:
                    novo_status = True
                case 2:
                    novo_status = False
            obra_escolhida["status"] = novo_status
        case 4:
            print(branco("Qual a categoria da obra? "))
            print(branco("[1] - Anime [2] - Mangá"))
            categoria = validarEscolha(input("Sua opção: "))
            match categoria:
                case 1:
                    nova_categoria = "Anime"
                case 2:
                    nova_categoria = "Manga"
            obra_escolhida["categoria"] = nova_categoria
        case 5:
            if not obra_escolhida["interesse"]:
                print(f"{branco("Deseja colocar a obra"), azul(obra_escolhida['nome']), branco('na lista de interesses:')} ")
                print(vermelho("A AÇÃO IRÁ COLOCAR ALGUMAS INFOMAÇÕES COMO DEFAULT, DESEJA CONTINUAR?"))
                print(f'{amarelo('[1]')} {vermelho('SIM')} {amarelo('[2]')} {verde('NÃO')}')
                opc = validarEscolha(input("Sua opção: "))
                if opc == 1:
                    obra_escolhida["interesse"] = True
                    obra_escolhida["status"] = False
                    obra_escolhida['nota'] = 0
                    obra_escolhida['analise'] = "<SEM ANALISE>"
                else:
                    return
            else:
                obra_escolhida["interesse"] = False
                print(branco("O que achou da obra? "))
                notas()
                obra_escolhida['nota'] = validarNota(input("Sua opção: "))
                concluidoOpcao()
                novo_status = validarEscolha(input("Sua opção: "))
                match novo_status:
                    case 1:
                        novo_status = True
                    case 2:
                        novo_status = False
                obra_escolhida["status"] = novo_status
                print(branco("Deseja adicionar uma breve analise da obra? "))
                print(branco("[1] - SIM [2] - Não"))
                opc = validarEscolha(input("Sua Opção: "))

                if opc == 1:
                    obra_escolhida['analise'] = input("Digite sua analise da obra: ")
                    if obra_escolhida['analise'].strip() == "":
                        obra_escolhida['analise'] = "<SEM ANALISE>"
                else:
                    obra_escolhida['analise'] = "<SEM ANALISE>"
        case 6:
            if obra_escolhida["interesse"]:
                print(msg)
                return
            nova_analise = (input("Digite a nova analise da obra: "))
            if nova_analise.strip() == "":
                obra_escolhida["analise"] = "<SEM ANALISE>"
            else:
                obra_escolhida["analise"] = nova_analise
        case 7:
            print(verde("Retornando ao Menu..."))
            sleep(1)
            return
    if salvarObras(obras):
        print(verde('OBRA ATUALIZADA COM SUCESSO!'))
    else:
        print(vermelho('NÃO FOI POSSÍVEL EDITAR A OBRA'))

def deletar():
    obras = carregarObras()
    if obras is None:
        return
    if len(obras) == 0:
        print(vermelho("NENHUMA OBRA CADASTRADA!"))
        return
    mostrarObrasSelecao(obras)
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
            if salvarObras(obras):
                print(verde(f"OBRA {azul(nome_excluido)} | {azul(categoria_excluido)} {verde("DELETADA COM SUCESSO!")}"))
            else:
                print(vermelho('NÃO FOI POSSIVEL DELETAR A OBRA'))
            sleep(1)

        case 2:
            print(verde("Retornando ao menu..."))
            sleep(1)
            return
def validarObrasImportadas(obras):
    if type(obras) != list:
        return False
    chaves = ("nome", "nota", "status", "categoria", "interesse", "analise")
    for obra in obras:
        if type(obra) != dict:
            return False
        for chave in chaves:
            if chave not in obra:
                return False
        if len(obra) != len(chaves):
            return False
        if type(obra['nome']) != str or obra['nome'].strip() == "":
            print(vermelho("Nome não é um valor válido"))
            return False
        if type(obra['nota']) != int or obra['nota']  > 10 or obra['nota'] < 0:
            print(vermelho("Nota não é um valor válido"))
            return False
        if type(obra['status']) != bool:
            print(vermelho("Conclusão não é um valor válido"))
            return False
        if type(obra['categoria']) != str or obra['categoria'] not in ["Anime", "Manga"]:
            print(vermelho("Categoria não é um valor válido"))
            return False
        if type(obra['interesse']) != bool:
            print(vermelho("Interesse não é um valor válido"))
            return False
        if type(obra['analise']) != str:
            print(vermelho("Analise não é um valor válido"))
            return False
        if obra['interesse']:
            if obra['status'] != False:
                return False
            if obra['nota'] != 0:
                return False
            if obra['analise'] != "<SEM ANALISE>":
                return False
    return True

def importarObras():
    print(branco("Como deseja importar as obras?"))
    print(f"{amarelo("[1]")} - {vermelho("Substituir atuais")} {amarelo("[2]")} - {verde("Acrescentar as atuais")}")
    opc = validarEscolha(input(f"Sua opção: "))
    try:
        with open('animes.json', mode='r', encoding='utf-8') as arquivo:
            obras_importadas = json.load(arquivo)
    except FileNotFoundError:
        print(vermelho("ERRO: NÃO FOI POSSÍVEL LOCALIZAR O ARQUIVO"))
        return False
    except json.JSONDecodeError:
        print(vermelho("ERRO: ARQUIVO JSON INVÁLIDO!"))
        return False
    else:
        print(branco("Validando obras..."))
        if validarObrasImportadas(obras_importadas):
            sleep(1)
            print(verde("OBRAS VALIDADAS"))
            if opc == 1:
                obras_finais = obras_importadas
            else:
                obras_atuais = carregarObras()
                if obras_atuais is None:
                    return False
                for obra_imp in obras_importadas:
                    encontrou = False
                    for obra_atu in obras_atuais:
                        if obra_imp['nome'].strip().lower() == obra_atu['nome'].strip().lower() and obra_imp['categoria'] == obra_atu['categoria']:
                            encontrou = True
                            print(
                                f"A obra {azul(obra_imp['nome'])} | {azul(obra_imp['categoria'])} "
                                f"já existe. Deseja manter ambas ou substituir?"
                            )
                            print(f"{amarelo('[1]')} - {branco("Manter ambas")}")
                            print(f"{amarelo('[2]')} - {branco("Substituir")}")
                            opcao = validarEscolha(input(f"Sua opção: "))
                            if opcao == 1:
                                obras_atuais.append(obra_imp)
                            else:
                                indice = obras_atuais.index(obra_atu)
                                obras_atuais[indice] = obra_imp
                            break
                    if not encontrou:
                        obras_atuais.append(obra_imp)

                obras_finais = obras_atuais
            if salvarObras(obras_finais):
                print(verde("OBRAS IMPORTADAS COM SUCESSO"))
                return True
            else:
                print(vermelho("NÃO FOI POSSÍVEL SALVAR AS OBRAS IMPORTADAS"))
                return False
        else:
            print(vermelho("OCORREU UM ERRO AO VALIDAR AS OBRAS"))
            return False
def exportarObras():
    obras = carregarObras()
    if obras is None:
        return
    try:
        with open('animes.json', mode='w', encoding='utf-8') as arquivo:
            json.dump(obras, arquivo, indent=4, ensure_ascii=False)
    except PermissionError:
        print(vermelho("ERRO: SEM PERMISSÃO PARA ESCREVER NO ARQUIVO."))
        return False
    except OSError:
        print(vermelho("ERRO: OCORREU UM PROBLEMA AO ACESSAR O ARQUIVO."))
        return False
    else:
        print(verde("OBRAS EXPORTADAS COM SUCESSO"))
        return True

