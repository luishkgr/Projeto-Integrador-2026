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
