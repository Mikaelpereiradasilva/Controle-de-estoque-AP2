
import crede
import escolas
import util
import json
import os


# Menu principal do sistema
def menu_principal():
    while True:
        util.limpa_tela()
        util.cabecalho()

        print(
            "Seja bem-vindo ao Sistema de Controle "
            "de Estoque Escolar!\n"
        )
        print("1 - Sou CREDE")
        print("2 - Sou Escola")
        print("0 - Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            login_crede()
        elif opcao == '2':
            login_escola()
        elif opcao == '0':
            print("\nEncerrando o sistema. Até logo!\n")
            util.timer()
            break
        else:
            util.opcao_invalida()
            util.timer()


# Menu de acesso da CREDE
def login_crede():
    while True:
        util.limpa_tela()
        util.cabecalho()

        print("\n- Login CREDE -\n")
        print("1 - Cadastrar uma CREDE")
        print("2 - Já tenho cadastro")
        print("0 - Voltar")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            adm_cadastro_crede()
        elif opcao == '2':
            entrar_crede()
        elif opcao == '0':
            break
        else:
            util.opcao_invalida()
            util.timer()


# Menu de acesso da Escola
def login_escola():
    while True:
        util.limpa_tela()
        util.cabecalho()

        print("\n- Login Escola -\n")
        print("1 - Cadastrar-se como Escola")
        print("2 - Já tenho cadastro")
        print("0 - Voltar")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            cadastro_escola()
        elif opcao == '2':
            entrar_escola()
        elif opcao == '0':
            break
        else:
            util.opcao_invalida()
            util.timer()


# Cadastro de CREDE protegido por senha de administrador
def adm_cadastro_crede():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Cadastro CREDE -\n")
    print("Apenas para usuários autorizados.\n")

    prosseguir = util.senha_administrador()

    if prosseguir:
        cadastro_crede()

    util.timer()


# Cadastro de CREDE
def cadastro_crede():
    util.limpa_tela()
    util.cabecalho()

    credes = carregar_crede()

    print("\n- Cadastro CREDE -\n")

    codigo = input("Digite o código oficial da CREDE: ")

    for cadastro in credes:
        if cadastro["codigo"] == codigo:
            print("Código já cadastrado.")
            util.timer()
            return

    nome = input("Digite o nome da CREDE: ")
    senha = input("Crie a senha de acesso: ")

    print("\n- Confira os dados inseridos -\n")
    print(f"Código: {codigo}")
    print(f"Nome: {nome}")

    opcao = input(
        "Pressione 1 para confirmar ou 0 para cancelar: "
    )

    if opcao == '1':
        credes.append({
            "codigo": codigo,
            "nome": nome,
            "senha": senha
        })

        salvar_crede(credes)

        print("\nCadastro realizado com sucesso!\n")

    elif opcao == '0':
        print("\nCadastro cancelado.\n")

    else:
        print("\nOpção inválida. Cadastro não realizado.\n")

    util.timer()


# Carrega os cadastros de CREDE
def carregar_crede():
    if not os.path.exists("credes.json"):
        return []

    with open("credes.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# Salva os cadastros de CREDE
def salvar_crede(credes):
    with open("credes.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            credes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# Cadastro de Escola (a implementar)
def cadastro_escola():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Cadastro Escola -\n")
    print("Cadastro de Escola em breve...\n")

    util.timer()


# Entrada da CREDE
def entrar_crede():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Entrar como CREDE -\n")

    # A autenticação será implementada na próxima etapa.
    crede.menu_principal()

    util.timer()


# Entrada da Escola
def entrar_escola():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Entrar como Escola -\n")

    # A autenticação será implementada posteriormente.
    escolas.menu_principal()

    util.timer()


menu_principal()
