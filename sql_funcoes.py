# Biblioteca do Curso Python 536 para Banco de Dados

# OBS: As funções ter as 4 etapas 
# 1. Iniciar Conexão
# 2. CRUD/Query
# 3. Commit
# 4. Finalizar a Conexão/ Close

# def nomeFuncao (entradas):

import sqlite3
import os


# ----------------------------- CRIAR TABELA ----------------------------------
# Conexão
def criarTabela(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    queryCriarTabela = '''CREATE TABLE IF NOT EXISTS "Contatos" (
    "id"	INTEGER,
    "nome"	TEXT,
    "sobrenome"	TEXT,
    "email"	TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);'''
    cursor.execute(queryCriarTabela)
# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()

# ----------------------------- iNSERIR DADOS ----------------------------------
# Conexão
def inserirDados(db,nome,sobrenome,email):
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    # nome = str(input("Digite o seu nome: "))
    # sobrenome = str(input("Digite o seu sobrenome: "))
    # email = str(input("Digite o seu email: "))
    query = f'''INSERT INTO "Contatos" (nome, sobrenome, email)
    VALUES("{nome}","{sobrenome}","{email}");'''

    cursor.execute(query)
# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
# ----------------------------- ATUALIZAR DADOS --------------------------------
# Conexão
def atualizarDados(db, nome, sobrenome, email, numRegistro):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    # nome = input("Digite seu novo nome: ")
    # numRegistro = int(input("Digite o número do registro: "))

    if len(nome) != 0 and nome != '\r':

        queryAtualizarDados = f'''
            UPDATE "Contatos"
            SET nome = "{nome}"
            WHERE id="{numRegistro}"
        '''

        cursor.execute(queryAtualizarDados)

    if len(nome) != 0 and nome != '\r':

        queryAtualizarDados = f'''
            UPDATE "Contatos"
            SET sobrenome = "{sobrenome}"
            WHERE id="{numRegistro}"
        '''

        cursor.execute(queryAtualizarDados)

    if len(nome) != 0 and nome != '\r':

        queryAtualizarDados = f'''
            UPDATE "Contatos"
            SET email = "{email}"
            WHERE id="{numRegistro}"
        '''

        cursor.execute(queryAtualizarDados)
# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
# ----------------------------- APAGAR DADOS -----------------------------------
# Conexão
def apagarDados(db,apagarReg):
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    # apagarReg = int(input("Digite o id que deseja apagar: "))
    queryApagarDados = f'''
    DELETE FROM "Contatos" 
    WHERE id="{apagarReg}"'''

    cursor.execute(queryApagarDados)
# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
# ----------------------------- SELECIONAR DADOS - TODOS -------------------------------
# Conexão
def selecionarDadosTodos(db):
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    queryselecionarReg = '''
                SELECT * FROM "Contatos"  
    '''
    cursor.execute(queryselecionarReg)
    dados = cursor.fetchall()

# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
    return dados
# ----------------------------- SELECIONAR DADOS - PARCIAL -------------------------------
# Conexão
def selecionarDadosParcial(db,primeiroRegistro, quantidade):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    #id = input("Digite o id da pessoa que você quer selecionar: ")
    
    queryParcial = f'''
        SELECT * FROM "Contatos" 
        WHERE id >= {primeiroRegistro}
        LIMIT {quantidade}
    '''

    cursor.execute(queryParcial)

    dados = cursor.fetchall()

# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
    return dados
# ----------------------------- SELECIONAR DADOS - ID -------------------------------
# Conexão
def selecionarDadosId(db,selectid):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

# CRUD
    #selectid = int(input("Digite o id que deseja selecionar: "))
    querySelectId = f'''
        SELECT * FROM "Contatos" 
        WHERE id="{selectid}"
    '''
        

    cursor.execute(querySelectId)
    dados = cursor.fetchall()

# COMMIT
    conn.commit()
# Fechar Conexão
    conn.close()
    return dados