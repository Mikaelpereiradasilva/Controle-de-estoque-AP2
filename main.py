
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
    
    cnpj = input("Digite o CNPJ da CREDE: ")

    cnpj = util.padronizar_cnpj(cnpj)
    
    while True:
        if cnpj is not None:
            break
        else:
            print("\nCNPJ inválido! Por favor, digite um CNPJ válido.\n")
            cnpj = input("Digite o CNPJ da CREDE: ")
            cnpj = util.padronizar_cnpj(cnpj)
    
    for cadastro in credes:
        if cadastro["cnpj"] == cnpj:
            print("CNPJ já cadastrado.")
            util.timer()
            return

    

    nome = input("Digite o nome da CREDE: ")
    senha = input("Crie a senha de acesso: ")

    salt, senha_hash = util.gerar_hash_senha(senha)

    print("\n- Confira os dados inseridos -\n")
    print(f"CNPJ: {cnpj}")
    print(f"Nome: {nome}")

    opcao = input("\nPressione 1 para confirmar ou 0 para cancelar: \n")

    if opcao == '1':
        credes.append({
            "cnpj": cnpj,
            "nome": nome,
            "salt": salt,
            "senha_hash": senha_hash
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
        conteudo = arquivo.read().strip()

    if not conteudo:
        return []

    return json.loads(conteudo)



# Salva os cadastros de CREDE

def salvar_crede(credes):
    with open("credes.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            credes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

# Entrada da CREDE
def entrar_crede():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Entrar como CREDE -\n")

    cnpj = input("Digite o CNPJ da CREDE: ")
    cnpj = util.padronizar_cnpj(cnpj)
    while True:
            if cnpj is not None:
                break
            else:
                print("\nCNPJ inválido! Por favor, digite um CNPJ válido.\n")
                cnpj = input("Digite o CNPJ da CREDE: ")
                cnpj = util.padronizar_cnpj(cnpj)
    senha = input("Digite a senha de acesso: ")
    credes = carregar_crede()
    for cadastro in credes:
        if cadastro["cnpj"] == cnpj:
            if util.verificar_senha(
                senha,
                cadastro["salt"],
                cadastro["senha_hash"]
            ):
                print("\nLogin realizado com sucesso!\n")
                util.timer()
                crede.menu_principal()
                return

    print("\nCNPJ ou senha incorretos! Tente novamente.\n")
    util.timer()
    return

# Cadastro de Escola (a implementar)
def cadastro_escola():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Cadastro Escola -\n")
    print("Cadastro de Escola em breve...\n")

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
