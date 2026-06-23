import customtkinter as ctk
from .componentes import *
import sqlite3
from telas.componentes import *

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
        width=800,
        height=500,
        border_width=1,
        border_color=COR_PRETO,
        corner_radius=4,
        fg_color=COR_BRANCO
    )
    frame_add_funcionario.grid(row=1, column=0, columnspan=3, pady=20)
    frame_add_funcionario.grid_propagate(False)

    frame_add_funcionario.grid_columnconfigure(0, weight=1)
    frame_add_funcionario.grid_columnconfigure(1, weight=1)

#endregion

    #region add nome

    labela_nome = ctk.CTkLabel(
        frame_add_funcionario,
        text="Nome",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    labela_nome.grid(row=0, column=0, pady=(50,0))

    entry_nome = ctk.CTkEntry(
        frame_add_funcionario,
        width=220,
        height=25,
        placeholder_text="Digite o nome",
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    entry_nome.grid(row=1, column=0, pady=10)

    #endregion

    #region cargo

    label_cargo = ctk.CTkLabel(
        frame_add_funcionario,
        text="Cargo",
        font=("Segoe UI Semibold", 15),
    )
    label_cargo.grid(row=0, column=1, pady=(50,0))

    combo_cargo = ctk.CTkComboBox(
        frame_add_funcionario,
        width=220,
        height=25,
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    combo_cargo.grid(row=1, column=1, pady=10)

    #endregion

    #region registro profissional

    label_registro = ctk.CTkLabel(
        frame_add_funcionario,
        text="Registro Profissional",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    label_registro.grid(row=2, column=0, pady=(30,5))

    entry_registro = ctk.CTkEntry(
        frame_add_funcionario,
        width=220,
        height=25,
        placeholder_text="Ex: CRM 12345",
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    entry_registro.grid(row=3, column=0, pady=5)

    #endregion

    #region telefone

    label_telefone = ctk.CTkLabel(
        frame_add_funcionario,
        text="Telefone",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    label_telefone.grid(row=2, column=1, pady=(30,5))

    entry_telefone = ctk.CTkEntry(
        frame_add_funcionario,
        width=220,
        height=25,
        border_width=1,
        placeholder_text="(00) 00000-0000)",
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    entry_telefone.grid(row=3, column=1, pady=5)

    #endregion

    #region email

    label_email = ctk.CTkLabel(
        frame_add_funcionario,
        text="Email",
        font=("Segoe UI Semibold", 15),
        text_color=COR_PRETO,
    )
    label_email.grid(row=4, column=0, pady=(30,5))

    entry_email = ctk.CTkEntry(
        frame_add_funcionario,
        width=220,
        height=25,
        placeholder_text="email@empresa.com",
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    entry_email.grid(row=5, column=0, pady=5)

    #endregion

    #region status

    label_status = ctk.CTkLabel(
        frame_add_funcionario,
        text="Status",
        font=("Segoe UI Semibold", 15),
    )
    label_status.grid(row=4, column=1, pady=(30,5))

    combo_status = ctk.CTkComboBox(
        frame_add_funcionario,
        width=220,
        height=25,
        border_width=1,
        corner_radius=3,
        font=("Segoe UI", 12),
        text_color=COR_PRETO
    )
    combo_status.grid(row=5, column=1, pady=5)

    #endregion

    #region botão salvar

    btn_salvar = botao_salvar(
        frame_add_funcionario,
        "Salvar",
    )
    btn_salvar.grid(row=6, column=0, columnspan=2, pady=40)

    #endregion














    #endregion