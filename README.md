# 📚 Gerenciador de Animes e Mangás

Projeto desenvolvido em Python para gerenciar animes e mangás assistidos, lidos ou que estão na lista de interesse.

O projeto foi criado com o objetivo de praticar conceitos fundamentais de Python, manipulação de arquivos e organização de dados.

## 🚀 Funcionalidades

- Cadastrar animes e mangás
- Separar obras consumidas da lista de interesses
- Avaliar obras com notas de 1 a 10
- Adicionar uma análise sobre a obra
- Informar se uma obra foi concluída ou está em andamento
- Editar obras cadastradas
- Excluir obras
- Listar obras com paginação
- Importar obras através de JSON
- Exportar obras para JSON
- Validar dados antes da importação
- Tratar conflitos entre obras durante a importação

## 🛠️ Tecnologias utilizadas

- Python
- JSON
- Manipulação de arquivos TXT
- Git e GitHub

## 📂 Estrutura do projeto

```text
Projetinho/
├── cores.py
├── funcoes.py
├── main.py
├── exemplo.json
├── README.md
└── .gitignore
```

### `main.py`

Arquivo principal responsável pela execução do programa e apresentação do menu.

### `funcoes.py`

Contém as funções utilizadas pelo sistema, como cadastro, edição, exclusão, listagem, importação e exportação.

### `cores.py`

Contém funções utilizadas para aplicar cores às mensagens exibidas no terminal.

### `exemplo.json`

Arquivo JSON de exemplo que pode ser utilizado para testar a funcionalidade de importação.

## ▶️ Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DO_REPOSITORIO
```

Execute:

```bash
python main.py
```

> É necessário ter o Python instalado para executar o projeto.

## 💾 Armazenamento dos dados

As obras cadastradas são armazenadas localmente no arquivo `animes.txt`.

Esse arquivo é criado/utilizado pelo programa e não precisa estar presente inicialmente.

A exportação dos dados é realizada utilizando o formato JSON.

## 📥 Importação

Ao importar um arquivo JSON, o programa valida a estrutura das obras antes de salvar os dados.

O usuário pode escolher entre:

- substituir as obras atuais;
- acrescentar as obras importadas às atuais.

Caso uma obra importada possua o mesmo nome e categoria de uma obra existente, o programa permite decidir como tratar o conflito.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como exercício prático de Python, trabalhando conceitos como:

- funções;
- listas;
- dicionários;
- estruturas condicionais;
- tratamento de exceções;
- leitura e escrita de arquivos;
- JSON;
- validação de dados;
- modularização;
- paginação.

## 📌 Status

Projeto funcional, ainda sujeito a melhorias e novas funcionalidades.