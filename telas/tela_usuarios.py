import customtkinter as ctk
from telas.componentes import *
from bancodedados.banco import listar_usuarios, atualizar_usuario


def mostrar_usuarios(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Usuários",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))

    card = ctk.CTkFrame(
        frame_conteudo,
        width=700,
        height=450,
        border_width=1,
        border_color=COR_CINZA,
        corner_radius=4,
        fg_color=COR_BRANCO,
    )
    card.grid(row=1, column=0, columnspan=3, pady=20)
    card.grid_propagate(False)
    card.grid_columnconfigure(0, weight=1)
    card.grid_columnconfigure(1, weight=1)

    label_selecao = ctk.CTkLabel(
        card,
        text="Selecione um usuário",
        font=("Segoe UI Semibold", 18),
        text_color=COR_PRETO,
    )
    label_selecao.grid(row=0, column=0, columnspan=2, pady=(30, 10))

    usuarios = listar_usuarios()
    opcoes = [f"{usuario[1]} ({usuario[2]})" for usuario in usuarios]
    usuarios_por_opcao = {opcao: usuario for opcao, usuario in zip(opcoes, usuarios)}

    combo_usuario = ctk.CTkComboBox(
        card,
        width=320,
        values=opcoes,
        state="readonly",
        font=("Segoe UI", 12),
    )
    combo_usuario.grid(row=1, column=0, columnspan=2, pady=10)

    if opcoes:
        combo_usuario.set(opcoes[0])

    label_nome = ctk.CTkLabel(card, text="Nome", font=("Segoe UI Semibold", 14), text_color=COR_PRETO)
    label_nome.grid(row=2, column=0, pady=(20, 5), sticky="w", padx=(60, 0))

    entry_nome = ctk.CTkEntry(card, width=260, placeholder_text="Nome do usuário")
    entry_nome.grid(row=3, column=0, padx=(60, 10), pady=5, sticky="w")

    label_login = ctk.CTkLabel(card, text="Login", font=("Segoe UI Semibold", 14), text_color=COR_PRETO)
    label_login.grid(row=2, column=1, pady=(20, 5), sticky="w", padx=(20, 0))

    entry_login = ctk.CTkEntry(card, width=260, placeholder_text="Login")
    entry_login.grid(row=3, column=1, padx=(20, 60), pady=5, sticky="w")

    label_senha = ctk.CTkLabel(card, text="Senha", font=("Segoe UI Semibold", 14), text_color=COR_PRETO)
    label_senha.grid(row=4, column=0, columnspan=2, pady=(20, 5))

    entry_senha = ctk.CTkEntry(card, width=260, placeholder_text="Senha", show="*")
    entry_senha.grid(row=5, column=0, columnspan=2, pady=5)

    status_label = ctk.CTkLabel(card, text="", font=("Segoe UI", 11), text_color=COR_VERDE)
    status_label.grid(row=6, column=0, columnspan=2, pady=(15, 0))

    def carregar_dados_usuario(event=None):
        opcao = combo_usuario.get()
        if not opcao or opcao not in usuarios_por_opcao:
            return

        usuario = usuarios_por_opcao[opcao]
        entry_nome.delete(0, "end")
        entry_login.delete(0, "end")
        entry_senha.delete(0, "end")
        entry_nome.insert(0, usuario[1])
        entry_login.insert(0, usuario[2])
        entry_senha.insert(0, usuario[3])
        status_label.configure(text="")

    def editar_usuario():
        opcao = combo_usuario.get()
        if not opcao or opcao not in usuarios_por_opcao:
            status_label.configure(text="Selecione um usuário primeiro.", text_color=COR_VERMELHO)
            return

        usuario = usuarios_por_opcao[opcao]
        nome = entry_nome.get().strip()
        login = entry_login.get().strip()
        senha = entry_senha.get().strip()

        if not nome or not login or not senha:
            status_label.configure(text="Preencha nome, login e senha.", text_color=COR_VERMELHO)
            return

        atualizar_usuario(usuario[0], nome, login, senha)
        status_label.configure(text="Usuário editado com sucesso.", text_color=COR_VERDE)

        usuarios_atualizados = listar_usuarios()
        opcoes_atualizadas = [f"{u[1]} ({u[2]})" for u in usuarios_atualizados]
        usuarios_por_opcao.clear()
        usuarios_por_opcao.update({opcao_atual: usuario_atual for opcao_atual, usuario_atual in zip(opcoes_atualizadas, usuarios_atualizados)})
        combo_usuario.configure(values=opcoes_atualizadas)
        combo_usuario.set(f"{nome} ({login})")

    combo_usuario.bind("<<ComboboxSelected>>", carregar_dados_usuario)

    if opcoes:
        carregar_dados_usuario()

    btn_editar = botao_azul(card, "Salvar", editar_usuario)
    btn_editar.grid(row=7, column=0, columnspan=2, pady=(20, 30))

    