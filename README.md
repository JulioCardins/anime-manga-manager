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
- SQLite (`sqlite3`)
- JSON
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

As obras cadastradas são armazenadas localmente em um banco de dados SQLite (obras.db).

O banco e a tabela são criados automaticamente pelo programa caso ainda não existam.

A troca de dados em formato JSON também é suportada para exportação e importação.

## 📥 Importação

Ao importar um arquivo JSON, o programa valida a estrutura das obras antes de salvar os dados.

O usuário pode escolher entre:

- substituir as obras atuais;
- acrescentar as obras importadas às atuais.

Caso uma obra importada possua o mesmo nome e categoria de uma obra existente, o programa permite decidir como tratar o conflito.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como exercício prático de Python, trabalhando conceitos como:

- funções;
- listas e dicionarios;
- estruturas condicionais;
- tratamento de exceções;
- banco de dados relacional com SQLite;
- JSON;
- validação de dados;
- modularização;
- paginação.

## 📌 Status

Em migração de armazenamento para SQLite, com fluxo principal funcional e sujeito a melhorias e novas funcionalidades.