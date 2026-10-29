
import credem
import escolas
import util
import json
import os
import credelc


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
            credelc.adm_cadastro_crede()
        elif opcao == '2':
            credelc.entrar_crede()
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
