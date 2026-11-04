
import escolas_login_e_cadastro
import util
import crede_login_e_cadastro


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
            crede_login_e_cadastro.adm_cadastro_crede()
        elif opcao == '2':
            crede_login_e_cadastro.entrar_crede()
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
            escolas_login_e_cadastro.adm_cadastro_escola()
        elif opcao == '2':
            escolas_login_e_cadastro.entrar_escola()
        elif opcao == '0':
            break
        else:
            util.opcao_invalida()
            util.timer()


menu_principal()
