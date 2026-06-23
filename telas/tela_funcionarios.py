import customtkinter as ctk
from telas.componentes import *
import sqlite3
import tela_add_funcionario
import tela_edit_funcionario

funcionario_selecionado = {"id": None}
linha_selecionada = {"labels": None}


#region FUNÇÕES

def busca_funci():
    conexao = sqlite3.connect("bancodedados/banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT 
            id,
            nome,
            cargo,
            registro_profissional,
            fone,
            email,
            status
        FROM profissional
    """)

    dados = cursor.fetchall()
    conexao.close()
    return dados

#endregion


#region config tela

def montar_tela_funcionarios(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="FUNCIONÁRIOS",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(30, 10))

    #endregion

    #region botões

    btn_add = botao_verde(
        frame_conteudo,
        "Adicionar funcionário +",
        comando=lambda: tela_add_funcionario.montar_tela_add_funcionario(frame_conteudo),
    )
    btn_add.grid(row=1, column=0, sticky="w", padx=17)

    #endregion

    #region info funcionários

    frame_info_funci = ctk.CTkFrame(frame_conteudo)
    frame_info_funci.grid(row=2, column=0, columnspan=3, pady=(10, 30))

    frame_funcionarios = ctk.CTkScrollableFrame(
        frame_info_funci,
        border_width=1,
        corner_radius=3,
        width=920,
        height=450,
        border_color="#000000"
    )
    frame_funcionarios.grid(row=0, column=0)

    larguras_colunas = [15, 170, 80, 160, 100, 150, 50, 150]

    for coluna, largura in enumerate(larguras_colunas):
        frame_funcionarios.grid_columnconfigure(coluna, minsize=largura, weight=0)

    cabecalhos = [
        "ID",
        "Nome",
        "Cargo",
        "Registro Profissional",
        "Fone",
        "Email",
        "Status",
        "Ações"
    ]

    for coluna, texto in enumerate(cabecalhos):
        label = ctk.CTkLabel(
            frame_funcionarios,
            text=texto,
            font=("Segoe UI Semibold", 14),
            width=larguras_colunas[coluna],
            anchor="w"
        )
        label.grid(
            row=0,
            column=coluna,
            pady=10,
            padx=5,
            sticky="w"
        )

    linha = ctk.CTkFrame(
        frame_funcionarios,
        height=2,
        fg_color="#adadad"
    )
    linha.grid(row=1, column=0, columnspan=8, sticky="ew", padx=5)

    def selecionar_funcionario(id_funcionario, labels_linha):
        if linha_selecionada["labels"] is not None:
            for label_antigo in linha_selecionada["labels"]:
                label_antigo.configure(fg_color="transparent")

        linha_selecionada["labels"] = labels_linha
        funcionario_selecionado["id"] = id_funcionario

        for label in labels_linha:
            label.configure(fg_color="#BFD7FF")

        print("Funcionário selecionado:", id_funcionario)

    funcionarios = busca_funci()

    for linha_tabela, funcionario in enumerate(funcionarios, start=2):
        id_funcionario = funcionario[0]
        labels_linha = []

        for coluna, valor in enumerate(funcionario):
            label = ctk.CTkLabel(
                frame_funcionarios,
                text=valor,
                width=larguras_colunas[coluna],
                anchor="w",
                justify="left",
                fg_color="transparent",
                corner_radius=4
            )

            label.grid(
                row=linha_tabela,
                column=coluna,
                pady=4,
                padx=5,
                sticky="w"
            )

            labels_linha.append(label)

        def entrar_mouse(event, labels=labels_linha):
            if linha_selecionada["labels"] != labels:
                for label in labels:
                    label.configure(fg_color="#E8F0FE")

        def sair_mouse(event, labels=labels_linha):
            if linha_selecionada["labels"] != labels:
                for label in labels:
                    label.configure(fg_color="transparent")

        def clicar(event, id_func=id_funcionario, labels=labels_linha):
            selecionar_funcionario(id_func, labels)

        for label in labels_linha:
            label.bind("<Enter>", entrar_mouse)
            label.bind("<Leave>", sair_mouse)
            label.bind("<Button-1>", clicar)

        frame_acoes = ctk.CTkFrame(
            frame_funcionarios,
            fg_color="transparent",
            width=larguras_colunas[7]
        )
        frame_acoes.grid(
            row=linha_tabela,
            column=7,
            pady=4,
            padx=5,
            sticky="w"
        )

        btn_editar = ctk.CTkButton(
            frame_acoes,
            text="Editar",
            width=35,
            height=20,
            font=("Segoe UI Semibold", 11),
            fg_color=COR_AZUL,
            hover_color=HOVER_AZUL,
            command=lambda id_func=id_funcionario: tela_edit_funcionario.montar_tela_editar_funcionario(frame_conteudo,id_func)
        )
        btn_editar.grid(row=0, column=0, padx=(0, 5))

        btn_excluir = ctk.CTkButton(
            frame_acoes,
            text="Excluir",
            width=35,
            height=20,
            font=("Segoe UI Semibold", 11),
            fg_color=COR_VERMELHO,
            hover_color=HOVER_VERMELHO,
            command=lambda id_func=id_funcionario: print("Excluir:", id_func)
        )
        btn_excluir.grid(row=0, column=1)

    #endregion