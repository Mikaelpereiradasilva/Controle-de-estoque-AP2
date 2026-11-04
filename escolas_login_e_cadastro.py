import util
import escolas
import os, json


# Cadastro de Escolas protegido por senha de administrador
def adm_cadastro_escola():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Cadastro Escola -\n")
    print("Apenas para usuários autorizados.\n")

    prosseguir = util.senha_administrador()

    if prosseguir:
        cadastro_escola()

    util.timer()







# Cadastro de Escola
def cadastro_escola():
    util.limpa_tela()
    util.cabecalho()

    escolas = carregar_escolas()


    print("\n- Cadastro Escola -\n")

    ########### BLOCO PRO CNPJ ###########
    cnpj = input("Digite o CNPJ da Escola: ")

    cnpj = util.padronizar_cnpj(cnpj)

    while True:
            if cnpj is not None:
                break
            else:
                print("\nCNPJ inválido! Por favor, digite um CNPJ válido.\n")
                cnpj = input("Digite o CNPJ da Escola: ")
                cnpj = util.padronizar_cnpj(cnpj)

    for cadastro in escolas:
            if cadastro["cnpj"] == cnpj:
                print("CNPJ já cadastrado.")
                util.timer()
                return
    ############################################
    
    nome = input("Digite o nome da Escola: ")
    senha = input("Crie a senha de acesso: ")
    crede = input("Digite o CNPJ da CREDE vinculada a esta escola: ")

    salt, senha_hash = util.gerar_hash_senha(senha)

    util.limpa_tela()
    util.cabecalho()

    print("\n- Confira os dados inseridos: -\n")
    print("CNPJ: {}".format(cnpj))
    print("Nome: {}".format(nome))
    print("CREDE: {}".format(crede))

    opcao = input("\nEscreva 1 para confirmar ou 0 para cancelar: \n")

    if opcao == '1':
        escolas.append({
            "cnpj": cnpj,
            "nome": nome,
            "crede": crede,
            "salt": salt,
            "senha_hash": senha_hash
        })

        salvar_escolas(escolas)

        print("\nCadastro realizado com sucesso!\n")
    
    elif opcao == '0':
        print("\nCadastro cancelado.\n")

    else:
        print("\nOpção inválida. Cadastro não realizado.\n")

    util.timer()








# Carrega os cadastros de Escolas
def carregar_escolas():
    if not os.path.exists("lista_de_escolas.json"):
        return []

    with open("lista_de_escolas.json", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()

    if not conteudo:
        return []

    return json.loads(conteudo)






def salvar_escolas(escolas):
    with open("lista_de_escolas.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            escolas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )




# Entrada da Escola
def entrar_escola():
    util.limpa_tela()
    util.cabecalho()

    print("\n- Entrar como Escola -\n")

    cnpj = input("Digite o CNPJ da Escola: ")
    cnpj = util.padronizar_cnpj(cnpj)
    while True:
            if cnpj is not None:
                break
            else:
                print("\nCNPJ inválido! Por favor, digite um CNPJ válido.\n")
                cnpj = input("Digite o CNPJ da Escola: ")
                cnpj = util.padronizar_cnpj(cnpj)
    senha = input("Digite a senha de acesso: ")
    lista_escolas = carregar_escolas()
    for cadastro in lista_escolas:
        if cadastro["cnpj"] == cnpj:
            if util.verificar_senha(
                senha,
                cadastro["salt"],
                cadastro["senha_hash"]
            ):
                print("\nLogin realizado com sucesso!\n")
                util.timer()
                escolas.menu_principal()
                return

    print("\nCNPJ ou senha incorretos! Tente novamente.\n")
    util.timer()
    return
