import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox
from telas import tela_inicio
from telas import tela_escalas
from telas import tela_plantoes
from telas import tela_funcionarios
from telas import tela_relatorios
from telas import tela_usuarios
from telas.componentes import *
from datetime import datetime

#region config tela
def montar_tela_principal(container):
    container.title("Sistema de Horários e Escala de Plantão")
    container.geometry("1200x700")
    container.resizable(False, False)
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(1, weight=1) 
    container.grid_columnconfigure(0, weight=0)
    container.grid_columnconfigure(1, weight=0)

    largura = 1200
    altura = 700

    largura_tela = container.winfo_screenwidth()
    altura_tela = container.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    container.geometry(f"{largura}x{altura}+{x}+{y}")

    #endregion

    #region menu lateral

        #region titulo

    menu_topo = ctk.CTkFrame(
        container,
        height=120,
        fg_color="#ffffff",
        corner_radius=0
        
    )
    menu_topo.grid(row=0, column=1,sticky="ew")
    menu_topo.grid_propagate(False)
    menu_topo.grid_columnconfigure(0, weight=1)

    menu_lateral = ctk.CTkFrame(
        container,
        width=225,
        corner_radius=0,
        fg_color="#0B2A6F"
    )
    menu_lateral.grid(row=0, column=0,sticky="nsew",rowspan=2,)
    menu_lateral.grid_propagate(False)
    menu_lateral.grid_columnconfigure(0, weight=0)
    menu_lateral.grid_columnconfigure(1, weight=1)

    frame_conteudo = ctk.CTkFrame(
        container,
        width=975,
        height=700,
        fg_color="#f2f2f3",
        corner_radius=0
    )
    frame_conteudo.grid(row=1, column=1, sticky="nsew")
    frame_conteudo.grid_propagate(False)

    imagem_lateral = Image.open("telas/img/calen.png")

    img_lateral = ctk.CTkImage(
        light_image=imagem_lateral,
        dark_image=imagem_lateral,
        size=(70,70)
    )

    label_imagem = ctk.CTkLabel(
        menu_lateral,
        text="",
        image=img_lateral
    )
    label_imagem.grid(row=0, column=0, padx=(10, 5), pady=20)

    label_titulo = ctk.CTkLabel(
        menu_lateral,
        text="Gestão de Horários e \nEscalas de Plantão",
        font=("Segoe UI Semibold", 13),
        text_color="white"
    )
    label_titulo.grid(row=0, column=1, padx=0, pady=20, sticky="w")

    #endregion

        #region linha

    linha = ctk.CTkFrame(
        menu_lateral,
        height=2,
        fg_color="#1A3F85"  # azul um pouco mais claro
    )

    linha.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(10, 5))

        #endregion

        #region home

    frame_home = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_home.grid(row=2, column=0,columnspan=2, padx=20, pady=(20,5))
    frame_home.grid_propagate(False)

    img_home = Image.open("telas/img/home.png")

    img_btn_home = ctk.CTkImage(
        light_image=img_home,
        dark_image=img_home,
        size=(30,30)
    )

    btn_home = ctk.CTkButton(
        frame_home,
        text="  Início",
        image=img_btn_home,
        command=lambda: tela_inicio.mostrar_inicio(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_home.grid(row=0, column=0, sticky="nsew")

        #endregion

        #region escala

    frame_escala = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_escala.grid(row=3, column=0, columnspan=2, padx=20, pady=5)

    img_esc = Image.open("telas/img/calendar.png")

    img_btn_esc = ctk.CTkImage(
        light_image=img_esc,
        dark_image=img_esc,
        size=(30,30)
    )

    btn_escala = ctk.CTkButton(
        frame_escala,
        text="  Escalas",
        image=img_btn_esc,
        command=lambda: tela_escalas.mostrar_escalas(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_escala.grid(row=0, column=0, sticky="nsew")

        #endregion

        #region plantão

    frame_plantao = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
        )
    frame_plantao.grid(row=4, column=0, columnspan=2, padx=20, pady=5)

    img_plantao = Image.open("telas/img/plantao.png")

    img_btn_plantao = ctk.CTkImage(
        light_image=img_plantao,
        dark_image=img_plantao,
        size=(30,30)
    )

    btn_plantao = ctk.CTkButton(
        frame_plantao,
        text="  Plantões",
        image=img_btn_plantao,
        command=lambda: tela_plantoes.mostrar_plantoes(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_plantao.grid(row=0, column=0, sticky="nsew")


        #endregion

        #region funcionarios

    frame_func = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_func.grid(row=5, column=0, columnspan=2, padx=20, pady=5)

    img_func = Image.open("telas/img/group.png")

    img_btn_func = ctk.CTkImage(
        light_image=img_func,
        dark_image=img_func,
        size=(30,30)
    )

    btn_func = ctk.CTkButton(
        frame_func,
        text="  Funcionários",
        image=img_btn_func,
        command=lambda: tela_funcionarios.montar_tela_funcionarios(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_func.grid(row=0, column=0, sticky="nsew")


        #endregion

        #region linha 2

    linha = ctk.CTkFrame(
        menu_lateral,
        height=2,
        fg_color="#1A3F85"  # azul um pouco mais claro
    )

    linha.grid(row=6, column=0, columnspan=2, sticky="ew", padx=15, pady=(30, 10))

        #endregion

        #region relatorios

    frame_relatorios = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_relatorios.grid(row=7, column=0, columnspan=2, padx=20, pady=(20,10))

    img_relatorios = Image.open("telas/img/bar.png")

    img_btn_relatorios = ctk.CTkImage(
        light_image=img_relatorios,
        dark_image=img_relatorios,
        size=(30,30)
    )

    btn_relatorios = ctk.CTkButton(
        frame_relatorios,
        text=" Relatórios",
        image=img_btn_relatorios,
        command=lambda: tela_relatorios.mostrar_relatorios(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_relatorios.grid(row=0, column=0, sticky="nsew")


        #endregion

        #region gerenciar usuarios

    frame_usuario = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_usuario.grid(row=8, column=0, columnspan=2, padx=20, pady=(5,50))

    img_usuario = Image.open("telas/img/manage.png")

    img_btn_usuario = ctk.CTkImage(
        light_image=img_usuario,
        dark_image=img_usuario,
        size=(30,30)
    )

    btn_usuarios = ctk.CTkButton(
        frame_usuario,
        text="  Gerenciar usuário",
        image=img_btn_usuario,
        command=lambda: tela_usuarios.mostrar_usuarios(frame_conteudo),
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#1A3F85",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#0B2A6F",
        text_color="white"
    )
    btn_usuarios.grid(row=0, column=0, sticky="nsew")

        #endregion

        #region sair

    frame_logout = ctk.CTkFrame(
        menu_lateral,
        width=170,
        height=40,
        fg_color="transparent"
    )
    frame_logout.grid(row=9, column=0, columnspan=2, padx=20, pady=10)

    img_logout = Image.open("telas/img/logout.png")

    img_btn_logout = ctk.CTkImage(
        light_image=img_logout,
        dark_image=img_logout,
        size=(25,25)
    )

    btn_logout = ctk.CTkButton(
        frame_logout,
        text="  Sair",
        image=img_btn_logout,
        font=("Segoe UI Semibold", 15),
        compound="left",
        anchor="w",
        hover_color="#DC2626",
        cursor="hand2",
        width=170,
        height=40,
        fg_color="#EF4444",
        text_color="white"
    )
    btn_logout.grid(row=0, column=0, sticky="nsew")

        #endregion

        #region linha 3

    linha = ctk.CTkFrame(
        menu_lateral,
        height=2,
        fg_color="#1A3F85"  # azul um pouco mais claro
    )

    linha.grid(row=10, column=0, columnspan=2, sticky="ew", padx=15, pady=(30, 0))

        #endregion

        #region version

    frame_version = ctk.CTkFrame(
        menu_lateral,
        width=190,
        height=40,
        fg_color="transparent"
    )
    frame_version.grid(row=11, column=0, columnspan=2, padx=20, pady=10)

    img_version = Image.open("telas/img/verified2.png")

    img_labela_version = ctk.CTkImage(
        light_image=img_version,
        dark_image=img_version,
        size=(30,30)
    )

    label_version = ctk.CTkLabel(
        frame_version,
        text="      © 2026 Sistema de Horários\n e Escala de Plantão\n Versão 1.0.0",
        image=img_labela_version,
        font=("Segoe UI", 10),
        compound="left",
        anchor="w",
        text_color="white"
    )
    label_version.grid(row=0, column=0)
        #endregion

        #region notificações

    imagem_notificacao = Image.open("telas/img/notifications.png")

    img_btn_notification = ctk.CTkImage(
        light_image=imagem_notificacao,
        dark_image=imagem_notificacao,
        size=(25,25)
    )
    btn_notificacao = ctk.CTkButton(
        menu_topo,
        text="",
        image=img_btn_notification,
        fg_color="transparent",
        hover_color="#ebebeb",
        cursor="hand2",
        width=35,
        height=35,
    )
    btn_notificacao.grid(row=0, column=1, sticky="e",pady=15,)

        #endregion

        #region linha topo

    linha = ctk.CTkFrame(
        menu_topo,
        width=2,
        height=30,
        fg_color="#e2e2e2"  # azul um pouco mais claro
    )

    linha.grid(row=0, column=2, padx=15, pady=10)

    #endregion

        #region Usuario que esta usando o sistema

    frame_topo_usuario = ctk.CTkFrame(
        menu_topo,
        width=200,
        fg_color="transparent"
    )
    frame_topo_usuario.grid(row=0, column=3, padx=(10, 20), pady=5)


    label_nome = ctk.CTkLabel(
        frame_topo_usuario,
        text="Usuário",
        font=("Segoe UI Semibold", 12)
    )
    label_nome.grid(row=0, column=0, sticky="w")

    label_usuario = ctk.CTkLabel(
        frame_topo_usuario,
        text="Administrador",
        font=("Segoe UI Semibold", 11)
    )
    label_usuario.grid(row=1, column=0, sticky="w")




        #endregion


    #endregion

    tela_inicio.mostrar_inicio(frame_conteudo)
