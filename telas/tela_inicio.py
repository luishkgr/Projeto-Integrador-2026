import customtkinter as ctk
from telas.componentes import *
from PIL import Image
from datetime import datetime

#region config tela
def mostrar_inicio(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    cabecalho = ctk.CTkFrame(
        frame_conteudo,
        height=70,
        fg_color=COR_BRANCO,
        corner_radius=0
    )
    cabecalho.grid(row=0, column=0, columnspan=3, sticky="ew")
    cabecalho.grid_propagate(False)

    cabecalho.grid_columnconfigure(0, weight=1)
    cabecalho.grid_columnconfigure(1, weight=0)
    cabecalho.grid_columnconfigure(2, weight=0)

    frame_cards = ctk.CTkFrame(
        frame_conteudo,
        fg_color=COR_BRANCO,
        corner_radius=0,
        height=175
)
    frame_cards.grid(row=1, column=0,columnspan=3, sticky="ew")
    frame_cards.grid_propagate(False)
    frame_cards.grid_columnconfigure(0, weight=1)
    frame_cards.grid_columnconfigure(1, weight=1)
    frame_cards.grid_columnconfigure(2, weight=1)
    frame_cards.grid_columnconfigure(3, weight=1)

    frame_proximos_plantoes = ctk.CTkFrame(
        frame_conteudo,
        fg_color=COR_VERMELHO,
        corner_radius=15,
        height=360,
        border_width=2,
        border_color=COR_CINZA,
    )
    frame_proximos_plantoes.grid(row=2, column=0, columnspan=1, sticky="ew",pady=10, padx=15)



    #endregion

    #region linha topo
    linha_superior = ctk.CTkFrame(
        cabecalho,
        height=2,
        fg_color="#D3D3D3",
        corner_radius=0
    )
    linha_superior.place(relx=0, rely=0, relwidth=1, y=-1)

    #endregion

    #region saudações

    frame_saudacao = ctk.CTkFrame(
        cabecalho,
        width=300,
        height=60,
        fg_color="transparent"
    )
    frame_saudacao.grid(row=0, column=0, sticky="w", padx=15, pady=(20,0))
    frame_saudacao.grid_propagate(False)

    label_titulo = ctk.CTkLabel(
        frame_saudacao,
        text="Olá, Usuário",
        font=("Segoe UI", 18, "bold")
    )
    label_titulo.grid(row=0, column=0, sticky="w", pady=0)

    label_saudacao = ctk.CTkLabel(
        frame_saudacao,
        text="Bem-vindo ao Sistema de Horários e Escalas",
        font=("Segoe UI", 13)
    )
    label_saudacao.grid(row=1, column=0, sticky="w", pady=0)



    #endregion

#region cards

    #region card funcionarios

    frame_card_funcionarios = ctk.CTkFrame(
        frame_cards,
        width=200,
        height=120,
        fg_color=COR_BRANCO,
        border_width=2,
        border_color=COR_AZUL,
        corner_radius=5
    )
    frame_card_funcionarios.grid(row=0, column=0, pady=25)
    frame_card_funcionarios.grid_propagate(False)

    frame_circulo_funcionarios = ctk.CTkFrame(
        frame_card_funcionarios,
        width=60,
        height=60,
        corner_radius=100,
        fg_color=COR_AZUL_FUNDO
    )
    frame_circulo_funcionarios.grid(row=0, column=0, pady=20)

    imagem_funcionarios = Image.open(("telas/img/group_azul.png"))

    img_funcionarios = ctk.CTkImage(
        light_image=imagem_funcionarios,
        dark_image=imagem_funcionarios,
        size=(40,40)
    )

    label_img_funcionarios = ctk.CTkLabel(
        frame_card_funcionarios,
        text="",
        image=img_funcionarios,
        fg_color=COR_AZUL_FUNDO

    )
    label_img_funcionarios.grid(row=0, column=0, sticky="w",pady=40,padx=25)

    label_total_funcionarios = ctk.CTkLabel(
        frame_card_funcionarios,
        text="Funcionários",
        font=("Segoe UI" ,14, "bold")
    )
    label_total_funcionarios.grid(row=0, column=1,sticky="n", pady=10, padx=(0,20))

    #endregion

    #region card plantoes

    frame_card_plantoes = ctk.CTkFrame(
        frame_cards,
        width=200,
        height=120,
        fg_color=COR_BRANCO,
        border_width=2,
        border_color=COR_ROXO,
        corner_radius=5
    )
    frame_card_plantoes.grid(row=0, column=1, pady=5)
    frame_card_plantoes.grid_propagate(False)

    frame_circulo_plantoes = ctk.CTkFrame(
        frame_card_plantoes,
        width=60,
        height=60,
        corner_radius=100,
        fg_color=COR_ROXO_FUNDO
    )
    frame_circulo_plantoes.grid(row=0, column=0, pady=20)

    imagem_funcionarios = Image.open(("telas/img/medical.png"))

    img_calendario = ctk.CTkImage(
        light_image=imagem_funcionarios,
        dark_image=imagem_funcionarios,
        size=(40,40)
    )

    label_img_funcionarios = ctk.CTkLabel(
        frame_card_plantoes,
        text="",
        image=img_calendario,
        fg_color=COR_AZUL_FUNDO
    )
    label_img_funcionarios.grid(row=0, column=0, sticky="w",pady=40,padx=25)

    label_total_plantoes = ctk.CTkLabel(
        frame_card_plantoes,
        text= "Plantões",
        font=("Segoe UI", 14, "bold")
    )
    label_total_plantoes.grid(row=0, column=1,sticky="n", pady=10, padx=(0,20))


    #endregion

    #region card ausencias

    frame_card_ausencias = ctk.CTkFrame(
        frame_cards,
        width=200,
        height=120,
        fg_color=COR_BRANCO,
        border_width=2,
        border_color=COR_LARANJA,
        corner_radius=5
    )
    frame_card_ausencias.grid(row=0, column=2, pady=5)
    frame_card_ausencias.grid_propagate(False)

    frame_circulo_ausencias = ctk.CTkFrame(
        frame_card_ausencias,
        width=60,
        height=60,
        corner_radius=100,
        fg_color=COR_LARANJA_FUNDO
    )
    frame_circulo_ausencias.grid(row=0, column=0, pady=20)

    imagem_ausencias = Image.open(("telas/img/cancel.png"))

    img_ausencias = ctk.CTkImage(
        light_image=imagem_ausencias,
        dark_image=imagem_ausencias,
        size=(40,40)
    )

    label_img_ausencias = ctk.CTkLabel(
        frame_card_ausencias,
        text="",
        image=img_ausencias,
        fg_color=COR_LARANJA_FUNDO
    )
    label_img_ausencias.grid(row=0, column=0, sticky="w",pady=40,padx=25)

    label_total_ausencias = ctk.CTkLabel(
        frame_card_ausencias,
        text="Ausências",
        font=("Segoe UI", 14, "bold")
    )
    label_total_ausencias.grid(row=0, column=1,sticky="n", pady=10, padx=(0,20))

    #endregion

    #region card pendencias

    frame_card_pendencias = ctk.CTkFrame(
        frame_cards,
        width=200,
        height=120,
        fg_color=COR_BRANCO,
        border_width=2,
        border_color=COR_VERMELHO,
        corner_radius=5
    )
    frame_card_pendencias.grid(row=0, column=3, pady=5)
    frame_card_pendencias.grid_propagate(False)

    frame_circulo_pendencias = ctk.CTkFrame(
        frame_card_pendencias,
        width=60,
        height=60,
        corner_radius=100,
        fg_color=COR_FUNDO_VERMELHO
    )
    frame_circulo_pendencias.grid(row=0, column=0, pady=20)

    imagem_pendencias = Image.open("telas/img/warning.png")

    img_pendencias = ctk.CTkImage(
        light_image=imagem_pendencias,
        dark_image=imagem_pendencias,
        size=(40,40)
    )

    label_img_pendencias = ctk.CTkLabel(
        frame_card_pendencias,
        text="",
        image=img_pendencias,
        fg_color=COR_FUNDO_VERMELHO
    )
    label_img_pendencias.grid(row=0, column=0, sticky="w",pady=40,padx=25)

    label_total_pendencias = ctk.CTkLabel(
        frame_card_pendencias,
        text="Pendências",
        font=("Segoe UI", 14, "bold")
    )
    label_total_pendencias.grid(row=0, column=1,sticky="n", pady=10, padx=(0,20))

    #endregion

#endregion
