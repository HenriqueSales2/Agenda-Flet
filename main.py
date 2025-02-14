import flet as ft
import sql_funcoes as sf

def main(page: ft.Page):
    db = "agenda.db"
    
    sf.criarTabela(db)

    # FUNCOES DOS BOTOES DOS MENUS

    def ativarBtnInserir(e):
        if len(cxNome.value) != 0:
            btnInserir.disabled=False
        else:
            btnInserir.disabled=True

        page.update()
    
    def inserirDadosBtn(e):

        sf.inserirDados(db, cxNome.value, cxSobrenome.value, cxEmail.value)
        cxNome.value = ""
        cxSobrenome.value = ""
        cxEmail.value = ""
        page.update()

    def consultarIdBtn(e):
        dados = sf.selecionarDadosId(db,  cxId.value)

        if dados:
            dado = dados[0]

            cxNome.value = dado[1]
            cxSobrenome.value = dado[2]
            cxEmail.value = dado[3]
        else:
            cxNome.value = ""
            cxSobrenome.value = ""
            cxEmail.value = ""

        page.update()

    def atualizarDadosBtn():
        
        sf.atualizarDados(db, cxNome.value, cxSobrenome.value, cxEmail.value, cxId.value)

    def apagarDadosBtn():

        sf.apagarDados(db, int(cxId.value))
    
    # --------- COMPONENTES (OBJETOS) ---------

    txtId = ft.Text("Id")
    cxId = ft.TextField(
        label="Digite o numero do ID",
        text_align=ft.TextAlign.LEFT,
        
    )

    # Nome
    txtNome = ft.Text("Nome")
    cxNome = ft.TextField(
        label="Digite o Nome da Pessoa",
        text_align=ft.TextAlign.LEFT,
        on_change=ativarBtnInserir
    )

    # Sobrenome
    txtSobrenome = ft.Text("Sobrenome")
    cxSobrenome = ft.TextField(
        label="Digite o Sobrenome da Pessoa",
        text_align=ft.TextAlign.LEFT,

    )

    # Email
    txtEmail = ft.Text("Email")
    cxEmail = ft.TextField(
        label="Digite o Email da Pessoa",
        text_align=ft.TextAlign.LEFT,

    )

    # Botões
    btnInserir = ft.ElevatedButton("Cadastrar", disabled=True, on_click=inserirDadosBtn)
    btnatualizar = ft.ElevatedButton("Atualizar", on_click=atualizarDadosBtn)
    btnApagar = ft.ElevatedButton("Apagar", on_click=apagarDadosBtn)
    btnConsultarId = ft.ElevatedButton("Consultar", on_click=consultarIdBtn)

    #----- VARIAVEIS DE TELA PARA COLOCAR NO CONTENT DO BODY -----
    bodyInicial = ft.Text(
        "Programa de Agenda de Cliente"
    )

    bodyInserir = ft.Column(
    [
        txtNome,
        cxNome,
        txtSobrenome,
        cxSobrenome,
        txtEmail,
        cxEmail,
        btnInserir
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    bodyApagar = ft.Column(
    [
        txtId,
        cxId,
        btnConsultarId,
        txtNome,
        cxNome,
        txtSobrenome,
        cxSobrenome,
        txtEmail,
        cxEmail,
        btnApagar
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    bodyAtualizar = ft.Column(
    [
        txtId,
        cxId,
        btnConsultarId,
        txtNome,
        cxNome,
        txtSobrenome,
        cxSobrenome,
        txtEmail,
        cxEmail,
        btnatualizar
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )
    
    # FUNCOES DOS BOTOES DO APPBAR
    def menuInserir(e):
        body.content = bodyInserir
        page.update()

    def menuApagar(e):
        body.content = bodyApagar
        page.update()

    def menuAtualizar(e):
        body.content = bodyAtualizar
        page.update()
    
    # Menu de Opções
    page.appbar = ft.AppBar (
        leading=ft.Icon(ft.icons.DATASET),
        leading_width=40,
        title=ft.Text("Agenda de Cliente"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.ADD, on_click=menuInserir), # INSERIR DADOS
            ft.IconButton(ft.icons.REMOVE, on_click=menuApagar), # APAGAR DADOS
            ft.IconButton(ft.icons.UPDATE, on_click=menuAtualizar), # ATUALIZAR DADOS
            ft.IconButton(ft.icons.LIST_ALT_SHARP # SELECIONAR TODOS
                            )
                ]

    )

    # Corpo Principal (Body)

    body = ft.Container(
        content=bodyInicial
    )
    # Parte Central da Tela (Body - O que vai conter no body)
    page.add(
        body
    )

ft.app(target=main)