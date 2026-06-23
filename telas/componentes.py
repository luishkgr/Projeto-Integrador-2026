import customtkinter as ctk

COR_PRINCIPAL = "#0B2A6F"
COR_AZUL = "#3c48eb"
HOVER_AZUL = "#343ec9"
COR_VERDE = "#30b457"
HOVER_VERDE = "#2aa04d"
COR_VERMELHO = "#f31c1c"
HOVER_VERMELHO = "#f13535"
COR_BRANCO = "#fff"
COR_PRETO = "#000"
COR_CINZA = "#d3d3d3"
COR_AZUL_FUNDO ="#EAF1FF"
COR_VERDE_FUNDO ="#E7F8EE"
COR_ROXO_FUNDO ="#F2EAFB"
COR_ROXO = "#9333EA"
COR_LARANJA = "#F59E0B"
COR_LARANJA_FUNDO = "#FEF3E2"
COR_FUNDO_VERMELHO = "#FEE2E2"

def botao_azul(master, texto, comando=None):
    return ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        font=("Segoe UI Semibold", 12),
        text_color=COR_BRANCO,
        fg_color=COR_AZUL,
        hover_color=HOVER_AZUL,
        width=150,
        height=40,
    )

def botao_verde(master, texto, comando=None):
    return ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        font=("Segoe UI Semibold", 12),
        text_color=COR_BRANCO,
        fg_color=COR_VERDE,
        hover_color=HOVER_VERDE,
        width=130,
        height=30,
)


def botao_vermelho(master, texto, comando=None):
    return ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        font=("Segoe UI Semibold", 12),
        text_color=COR_BRANCO,
        fg_color=COR_VERMELHO,
        hover_color=HOVER_VERMELHO,
        width=150,
        height=40,
    )

def botao_salvar(master, texto, comando=None):
    return ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        font=("Segoe UI", 15, "bold"),
        text_color=COR_BRANCO,
        fg_color=COR_VERDE,
        hover_color=HOVER_VERDE,
        width=150,
        height=40
    )