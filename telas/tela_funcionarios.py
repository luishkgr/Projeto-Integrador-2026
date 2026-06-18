import customtkinter as ctk
from componentes import *
import sqlite3

#region FUNÇÕES
def busca_funci():
    conexao = sqlite3.connect("bancodedados.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM profissional")
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
        comando=lambda: print("Função em desenvolvimento"),
    )
    btn_add.grid(row=1,column=0, sticky="w", padx=80)

    frame_botoes = ctk.CTkFrame(
    frame_conteudo,
    fg_color="transparent"
)
    frame_botoes.grid(row=3, column=0, columnspan=3, pady=10)

    btn_edit = botao_azul(
        frame_botoes,
        "Editar funcionário",
        comando=lambda: print("Função em desenvolvimento"),
    )
    btn_edit.grid(row=0, column=0, padx=50)

    btn_del = botao_vermelho(
        frame_botoes,
        "Excluir funcionário",
        comando=lambda: print("Função em desenvolvimento")
    )
    btn_del.grid(row=0, column=1, padx=50)

    #endregion

    #region info funcionários

    frame_info_funci = ctk.CTkFrame(
        frame_conteudo
    )
    frame_info_funci.grid(row=2, column=0, columnspan=3, pady=(10,30))
    
    frame_funcionarios = ctk.CTkScrollableFrame(
        frame_info_funci,
        border_width=1,
        corner_radius=3,
        width=800,
        height=400,
        border_color="#000000"
    )
    frame_funcionarios.grid(row=0, column=0)
    frame_funcionarios.grid_columnconfigure(0, weight=1)
    frame_funcionarios.grid_columnconfigure(1, weight=4)
    frame_funcionarios.grid_columnconfigure(2, weight=3)
    frame_funcionarios.grid_columnconfigure(3, weight=2)


    label_id = ctk.CTkLabel(
        frame_funcionarios,
        text="ID",
        font=("Segoe UI Semibold", 14)
    )
    label_id.grid(row=0, column=0,pady=10, padx=10, sticky="ew")

    label_nome = ctk.CTkLabel(
        frame_funcionarios,
        text="Nome",
        font=("Segoe UI Semibold", 14)
    )
    label_nome.grid(row=0, column=1,pady=10, padx=10, sticky="ew")

    label_cargo = ctk.CTkLabel(
        frame_funcionarios,
        text="Cargo",
        font=("Segoe UI Semibold", 14)
    )
    label_cargo.grid(row=0, column=2,pady=10, padx=10, sticky="ew")

    label_status = ctk.CTkLabel(
        frame_funcionarios,
        text="Status",
        font=("Segoe UI Semibold", 14)
    )
    label_status.grid(row=0, column=3,pady=10, padx=10, sticky="ew")

    linha = ctk.CTkFrame(
        frame_funcionarios,
        height=2,
        fg_color="#adadad",
    )
    linha.grid(row=1, column=0, columnspan=4, sticky="ew", padx=10)

    funcionarios = busca_funci()

    for funcionario in funcionarios:
        id_funcionario = funcionario[0]
        nome = funcionario[1]
        cargo = funcionario[2]
        status = funcionario[3]

        ctk.CTkLabel(
            frame_funcionarios,
            text=id_funcionario
        ).grid(row=1, column=0, pady=8, padx=10, sticky="ew")

        ctk.CTkLabel(
            frame_funcionarios,
            text=nome
        ).grid(row=1, column=1, pady=8, padx=10, sticky="ew")

        ctk.CTkLabel(
            frame_funcionarios,
            text=cargo
        ).grid(row=1, column=2, pady=8, padx=10, sticky="ew")

        ctk.CTkLabel(
            frame_funcionarios,
            text=status
        ).grid(row=1, column=3, pady=8, padx=10, sticky="ew")

        edit_funcionario = ctk.CTkButton(
            frame_funcionarios,
            text="Editar",
            fg_color=COR_AZUL,
            hover_color=HOVER_AZUL,
            font=("Segoe UI Semibold", 10,),
            width=30,
            height=20
        )
        edit_funcionario.grid(row=1,column=4, padx=10)

        delete_funcionario = ctk.CTkButton(
            frame_funcionarios,
            text="Excluir",
            fg_color=COR_VERMELHO,
            hover_color=HOVER_VERMELHO,
            font=("Segoe UI Semibold", 10),
            width=30,
            height=20
        )
        delete_funcionario.grid(row=1,column=5)

    #endregion



