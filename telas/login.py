import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox

def montar_tela_login():

    login = entry_usuario.get()
    senha = entry_senha.get()

    if login and senha:
        CTkMessagebox(
            title = "Sucesso",
            message = "Login realizado com sucesso!",
            icon="check"
        )

    else:
        CTkMessagebox(
            title = "Erro",
            message = "Usuário ou senha Invalidos!",
            icon="cancel"
        )

##region configuração da tela

janela_login = ctk.CTk()
janela_login.title("Sistema de Horários e Escala de Plantão")
janela_login.geometry("1200x700")
janela_login.resizable(False, False)
janela_login.grid_rowconfigure(0, weight=1)
janela_login.grid_columnconfigure(0, weight=0)
janela_login.grid_columnconfigure(1, weight=0)

largura = 1200
altura = 700

largura_tela = janela_login.winfo_screenwidth()
altura_tela = janela_login.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

janela_login.geometry(f"{largura}x{altura}+{x}+{y}")

#endregion

    #region imagem lado equerdo

frame_esquerdo = ctk.CTkFrame(
    master=janela_login,
    fg_color="#0B2A6F",
    width=540,
    height=700,
    corner_radius=0
)
frame_esquerdo.grid(row=0, column=0, sticky="nsew")

imagem_original = Image.open("telas/img/imagem_login.png")

imagem_esquerda = ctk.CTkImage(
    light_image=imagem_original,
    dark_image=imagem_original,
    size=(540, 700)
)

label_imagem = ctk.CTkLabel(
    master=frame_esquerdo,
    text="",
    image=imagem_esquerda
)
label_imagem.grid(row=0, column=0, sticky="nsew")

#endregion

    #region config lado direito

frame_direito = ctk.CTkFrame(
    master=janela_login,
    fg_color="#d7d9dd",
    width=660,
    height=700,
)
frame_direito.grid(row=0, column=1,sticky="nsew")

frame_login = ctk.CTkFrame(
    frame_direito,
    fg_color="white",
    width=500,
    height=550
)
frame_login.grid(row=0, column=0,pady=(35,5), padx=80)
frame_login.grid_columnconfigure(0, weight=1)
frame_login.grid_propagate(False)

#endregion

    #region cabeçalho
icone = Image.open("telas/img/icone_user.png")

imagem_icone = ctk.CTkImage(
    light_image=icone,
    dark_image=icone,
    size=(80,80)
)

label_imagem_icone = ctk.CTkLabel(
    frame_login,
    text="",
    image=imagem_icone
)
label_imagem_icone.grid(row=0,column=0, columnspan=2,pady=(50,5),)


label_bem_vindo = ctk.CTkLabel(
    frame_login,
    text="Bem-vindo!",
    font=("Segoe UI", 29, "bold"),
    text_color="black"
)
label_bem_vindo.grid(row=1, column=0,columnspan=2)

label_descricao = ctk.CTkLabel(
    frame_login,
    text="Faça login para acessar o sistema",
    font=("Segoe UI", 15),
    text_color="#6B7280"
)
label_descricao.grid(row=2, column=0, columnspan=2, pady=10)

#endregion

    #region usuario

usuario = ctk.CTkFrame(
    frame_login,
    fg_color="transparent",
    width=400,
    height=100
)
usuario.grid(row=4,column=0, pady=0)
usuario.grid_propagate(False)

label_usuario = ctk.CTkLabel(
    usuario,
    text="Usuário",
    font=("Segoe UI ",15, "bold"),
    text_color="#111827"
)
label_usuario.grid(row=0, column=0, sticky="w",padx=25)

frame_entry_usuario = ctk.CTkFrame(
    usuario,
    width=350,
    height=45,
    fg_color="white",
    border_width=1,
    border_color="#D9DEE8",
    corner_radius=4
)
frame_entry_usuario.grid(row=1, column=0,padx=25)
frame_entry_usuario.grid_propagate(False)

icone_usuario = ctk.CTkLabel(
    frame_entry_usuario,
    text="👤",
    font=("Segoe UI ",30, "bold"),
    fg_color="transparent",
    text_color="#6B7280",
    width=40
)
icone_usuario.grid(row=0,column=0,sticky="w",padx=10,pady=5)

entry_usuario = ctk.CTkEntry(
    frame_entry_usuario,
    width=280,
    height=40,
    fg_color="white",
    border_width=0,
    corner_radius=0,
    border_color="#D9DEE8",
    placeholder_text="Digite seu usuário",
    placeholder_text_color="#9CA3AF",
    text_color="#111827"
)
entry_usuario.grid(row=0, column=1)

    #endregion

    #region senha

senha = ctk.CTkFrame(
    frame_login,
    fg_color="transparent",
    width=400,
    height=100
)
senha.grid(row=5, column=0, pady=0)
senha.grid_propagate(False)

label_senha = ctk.CTkLabel(
    senha,
    text="Senha",
    font=("Segoe UI ",15, "bold"),
    text_color="#111827"
)
label_senha.grid(row=0, column=0, sticky="w",padx=25)

frame_entry_senha = ctk.CTkFrame(
    senha,
    width=350,
    height=45,
    fg_color="white",
    border_width=1,
    border_color="#D9DEE8",
    corner_radius=4
)
frame_entry_senha.grid(row=1, column=0,padx=25)
frame_entry_senha.grid_propagate(False)

icone_senha = ctk.CTkLabel(
    frame_entry_senha,
    text="🔒",
    font=("Segoe UI ",30, "bold"),
    fg_color="transparent",
    text_color="#6B7280",
    width=40
)
icone_senha.grid(row=0, column=0, sticky="w",
padx=10, pady=5)

entry_senha = ctk.CTkEntry(
    frame_entry_senha,
    width=220,
    height=40,
    fg_color="white",
    border_width=0,
    corner_radius=0,
    border_color="#D9DEE8",
    placeholder_text="Digite sua senha",
    placeholder_text_color="#9CA3AF",
    text_color="#111827",
    show="*"
)
entry_senha.grid(row=0, column=1)

icone_visual = ctk.CTkFrame(
    frame_entry_senha,
    fg_color="transparent",
    width=40,
    height=40
)
icone_visual.grid(row=0,column=2)
senha_visivel = False

def mostrar_senha():
    global senha_visivel

    if senha_visivel:
        entry_senha.configure(show="*")
        botao_olho.configure(text="👁")
        senha_visivel = False
    else:
        entry_senha.configure(show="")
        botao_olho.configure(text="🕳")
        senha_visivel = True

botao_olho = ctk.CTkButton(
    icone_visual,
    text="👁",
    font=("Segoe UI ",25),
    width=35,
    height=35,
    fg_color="white",
    hover_color="#eeeded",
    text_color="black",
    border_width=0,
    command=mostrar_senha
)
botao_olho.grid(row=0, column=0, padx=(25,0))

    #endregion

    #region esqueceu a senha

esq_senha = ctk.CTkFrame(
    frame_login,
    fg_color="transparent",
    width=400,
    height=50
)
esq_senha.grid(row=6, column=0, pady=0)
esq_senha.grid_columnconfigure(0, weight=1)
esq_senha.grid_propagate(False)

link_senha = ctk.CTkButton(
    esq_senha,
    text="Esqueceu sua senha?",
    font=("Segoe UI Semibold", 14),
    width=100,
    height=40,
    fg_color="transparent",
    hover_color="white",
    text_color="#0649bc"
)
link_senha.grid(row=0, column=0, sticky="e", padx=(0,20))

def mouse_passou(event):
    link_senha.configure(text_color="#2563EB")
def mouse_saiu(event):
    link_senha.configure(text_color="#0649bc")

link_senha.bind("<Enter>", mouse_passou)
link_senha.bind("<Leave>", mouse_saiu)

    #endregion

    #region botão entrar

entrar = ctk.CTkFrame(
    frame_login,
    fg_color="transparent",
    width=400,
    height=50
)
entrar.grid(row=7, column=0, pady=(10,0))
entrar.grid_columnconfigure(0, weight=1)
entrar.grid_propagate(False)

frame_entrar = ctk.CTkFrame(
    entrar,
    fg_color="white",
    width=350,
    height=44,
    border_width=1,
    border_color="black"
)
frame_entrar.grid(row=0, column=0, pady=3)

img_entrar = Image.open("telas/img/login.png")

imagem_entrar = ctk.CTkImage(
    light_image=img_entrar,
    dark_image=img_entrar,
    size=(35,35)
)

btn_img_entrar = ctk.CTkButton(
    frame_entrar,
    fg_color="#0649bc",
    hover_color="#053A96",
    command= lambda: login(
        entry_senha.get(),
        entry_usuario.get()
    ),
    text="  Entrar",
    text_color="white",
    font=("Segoe UI Semibold",20),
    image=imagem_entrar,
    compound="left",
    border_width=0,
    width=350,
    height=40,
    corner_radius=6
)
btn_img_entrar.grid(row=0, column=0)


    #endregion

    #region rodapé

rodape = ctk.CTkFrame(
    frame_direito,
    width=500,
    height=70,
    fg_color="transparent"
)
rodape.grid(row=1, column=0, pady=(0,20))
rodape.grid_columnconfigure(0,weight=1)
rodape.grid_columnconfigure(1, weight=1)
rodape.grid_propagate(False)

img_verified = Image.open("telas/img/verified.png")

verified_rodape = ctk.CTkImage(
    light_image=img_verified,
    dark_image=img_verified,
    size=(30,30)
)

label_img_verified = ctk.CTkLabel(
    rodape,
    text="",
    image=verified_rodape
)
label_img_verified.grid(row=0, column=0, sticky="w", pady=20, padx=(100,0))

label_info = ctk.CTkLabel(
    rodape,
    text="© 2026 Sistema de Horários e Escala de Plantão\n Todos os direitos reservados.",
    font=("Segoe UI", 11)
)
label_info.grid(row=0, column=1, sticky="w",padx=(0,110))

    #endregion

janela_login.mainloop()