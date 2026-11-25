import sqlite3
from cores import vermelho
def criarBanco():
    conexao = sqlite3.connect("obras.db")
    cursor = conexao.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS obras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nota INTEGER NOT NULL,
                status INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                interesse INTEGER NOT NULL,
                analise TEXT NOT NULL
            )
        """)
    conexao.commit()
    conexao.close()

def adicionarObra(obra):
    conexao = sqlite3.connect("obras.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO obras (nome, nota, status, categoria, interesse, analise)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (obra['nome'],
              obra['nota'],
              obra['status'],
              obra['categoria'],
              obra['interesse'],
              obra['analise']
        ))

    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False

    else:
        conexao.commit()
        return True

    finally:
        conexao.close()

def buscarObras():
    conexao = sqlite3.connect("obras.db")
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    try:
        cursor.execute("""SELECT * FROM obras""")
        obras_banco = cursor.fetchall()

        obras = []

        for obra in obras_banco:
            obra_dict = dict(obra)
            obra_dict['status'] = bool(obra_dict['status'])
            obra_dict['interesse'] = bool(obra_dict['interesse'])
            obras.append(obra_dict)

    except sqlite3.Error as e:
        print(f"Erro: {e}")

    else:
        return obras

    finally:
        conexao.close()



def atualizarObras(id_obra, dados):
    if not isinstance(dados, dict) or not dados:
        return False

    colunas_permitidas = {"nome", "nota", "status", "categoria", "interesse", "analise"}

    for coluna in dados:
        if coluna not in colunas_permitidas:
            print(vermelho("COLUNA INVALIDA PARA ATUALIZAÇÃO"))
            return False

    set_clausulas = [f"{coluna} = ?" for coluna in dados]
    valores = list(dados.values())
    valores.append(id_obra)

    conexao = None
    try:
        conexao = sqlite3.connect("obras.db")
        cursor = conexao.cursor()
        comando = f"UPDATE obras SET {', '.join(set_clausulas)} WHERE id = ?"
        cursor.execute(comando, valores)
        conexao.commit()
        return True

    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False

    finally:
        if conexao:
            conexao.close()

def deletarObras(id_obra):
    conexao = sqlite3.connect("obras.db")
    cursor = conexao.cursor()

    try:
        comando = "DELETE from obras WHERE id = ?"
        cursor.execute(comando, (id_obra,))
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False
    else:
        return True
    finally:
        conexao.close()

