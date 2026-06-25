import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import sqlite3
from .componentes import *
from bancodedados.banco import cadastro_setor

def abrir_janela_add_cargo():

    janela_cargo = ctk.CTkToplevel()
    janela_cargo.title("Novo Cargo")
    janela_cargo.geometry("200x150")
    janela_cargo.resizable(False,False)
    janela_cargo.grab_set()
    janela_cargo.grid_columnconfigure(0, weight=1)

    largura = 300
    altura = 200

    largura_tela = janela_cargo.winfo_screenwidth()
    altura_tela = janela_cargo.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela_cargo.geometry(f"{largura}x{altura}+{x}+{y}")

    ctk.CTkLabel(
        janela_cargo,
        text="Adicionar um novo cargo",
        font=("Segoe UI", 16, "bold")
    ).grid(row=0, column=0, pady=20)

    entry_nome = ctk.CTkEntry(
        janela_cargo,
        font=("Segoe UI Semibold", 12),
        width=220,
        height=28,
        border_width=1,
        corner_radius=2,
        placeholder_text="Nome do cargo",
    )
    entry_nome.grid(row=1, column=0, pady=5)

    entry_descricao = ctk.CTkEntry(
        janela_cargo,
        font=("Segoe UI Semibold", 12),
        width=220,
        height=28,
        border_width=1,
        corner_radius=2,
        placeholder_text="Descrição",
    )
    entry_descricao.grid(row=2, column=0, pady=5)

    def salvar_cargo():
        nome = entry_nome.get().strip()
        descricao = entry_descricao.get().strip()
        
        if not nome:
            CTkMessagebox(title="Erro", message="Digite um nome para o cargo!")
            return
        
        try:
            cadastro_setor(nome, descricao)
            CTkMessagebox(title="Sucesso", message="Cargo salvo com sucesso!")
            janela_cargo.destroy()
        except Exception as e:
            CTkMessagebox(title="Erro", message=f"Erro ao salvar: {str(e)}")

    btn_salvar = botao_salvar(janela_cargo, "Salvar", salvar_cargo)
    btn_salvar.grid(row=3, column=0, pady=20)

