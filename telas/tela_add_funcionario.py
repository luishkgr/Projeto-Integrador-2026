import customtkinter as ctk
from componentes import *
import sqlite3

#region config tela

def montar_tela_add_funcionario(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="ADICIONAR FUNCIONÁRIO",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(30, 10))

    frame_add_funcionario = ctk.CTkFrame(
        frame_conteudo,
        width=900,
        height=500,
        border_width=1,
        border_color=COR_PRETO,
        corner_radius=4,
        fg_color=COR_BRANCO
    )
    frame_add_funcionario.grid(row=1, column=0, columnspan=3)
    frame_add_funcionario.grid_propagate(False)

#endregion

    #region add nome

    labela_nome = ctk.CTkLabel(
        frame_add_funcionario,
        text="Nome",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    labela_nome.grid(row=0, column=0, pady=(50,0), padx=100)

    entry_nome = ctk.CTkEntry(
        frame_add_funcionario,
        width=250,
        height=25,
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    entry_nome.grid(row=1, column=0, pady=5, padx=100)

    #endregion

    #region cargo

    label_cargo = ctk.CTkLabel(
        frame_add_funcionario,
        text="Cargo",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    label_cargo.grid(row=0, column=1, pady=(50,0), padx=100)

    combo_cargo = ctk.CTkComboBox(
        frame_add_funcionario,
        width=250,
        height=25,
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    combo_cargo.grid(row=1, column=1,pady=5, padx=100)


    #endregion