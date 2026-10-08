import sqlite3

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
            obras.append(dict(obra))

    except sqlite3.Error as e:
        print(f"Erro: {e}")

    else:
        return obras

    finally:
        conexao.close()



def atualizarObras(id_obra, coluna, novo_valor):
    conexao = sqlite3.connect("obras.db")
    cursor = conexao.cursor()

    try:
        comando = f"UPDATE obras SET {coluna} = ? WHERE id = ?"
        cursor.execute(comando, (novo_valor, id_obra))
        conexao.commit()

    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False

    else:
        return True

    finally:
        conexao.close()
