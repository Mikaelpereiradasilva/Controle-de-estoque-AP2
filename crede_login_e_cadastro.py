#Aqui estão os códigos de login e cadastro(lc) da Crede
import crede_menus
import util
import json
import os

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

    print("\n- Confira os dados inseridos: -\n")
    print(f"CNPJ: {cnpj}")
    print(f"Nome: {nome}")

    opcao = input("\nEscreva 1 para confirmar ou 0 para cancelar: \n")

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
    if not os.path.exists("lista_de_credes.json"):
        return []

    with open("lista_de_credes.json", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()

    if not conteudo:
        return []

    return json.loads(conteudo)



# Salva os cadastros de CREDE

def salvar_crede(credes):
    with open("lista_de_credes.json", "w", encoding="utf-8") as arquivo:
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
                crede_menus.menu_principal(cnpj_crede_logada=cnpj)
                return

    print("\nCNPJ ou senha incorretos! Tente novamente.\n")
    util.timer()
    return

