import crede
import escolas
import util



def menuPrincipal():
    while True:
        util.limpa_tela();
        util.cabecalho();
        print("- Como deseja acessar? -");
        print("1 - CREDE");
        print("2 - Escolas");
        print("0 - Sair");
        
        opcao = input("Selecione o tipo de acesso: ")
        
        if opcao == '1':
            crede.menu_principal()
        elif opcao == '2':
            print("\nSistema Escolar...\n")
            escolas.menu_principal() 
        elif opcao == '0':
            print("\nA encerrar o sistema principal. Até breve!\n")
            break
        else:
            print("\nOpção inválida! Por favor, digite 0, 1 ou 2.\n")

# Aqui está o menu principal de login, onde o usuário pode escolher entre acessar como CREDE ou como Escola.
def escolha_login():
    opcao = 3
    while opcao != 0:
        util.limpa_tela()
        util.cabecalho()
        print('Seja Bem-Vindo a o Sistema de Controle de Estoque Escolar!\nComo deseja acessar?')
        print()
        print("1 - Sou Crede")
        print("2 - Sou Escola")
        print("0 - Sair")
        print()
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            login_crede()
        elif opcao == 2:
            login_escola()
        elif opcao == 0:
            print("\nEncerrando o sistema. Até logo!\n")
            util.timer()
        else:
            util.opcao_invalida()
            util.timer()

#Aqui está o menu de login para usuários do tipo CREDE
def login_crede():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Login CREDE -\n")
    print('1 - Cadastar-se como CREDE')
    print('2 - Já tenho cadastro')
    print('0 - Voltar')
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        cadastro_crede()
    elif opcao == 2:
        entrar_crede()
    elif opcao == 0:
        escolha_login()
    else:
        util.opcao_invalida()
    util.timer()

#Aqui está o menu de login para usuários do tipo Escola
def login_escola():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Login Escola -\n")
    print('1 - Cadastar-se como Escola')
    print('2 - Já tenho cadastro')
    print('0 - Voltar')
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        cadastro_escola()
    elif opcao == 2:
        entrar_escola()
    elif opcao == 0:
        escolha_login()
    else:
        util.opcao_invalida()
    util.timer()

#Sessão de cadastro para CREDE e Escola, onde os usuários podem se registrar no sistema. Atualmente, essas funções estão em desenvolvimento e exibem mensagens de "em breve".
def cadastro_crede():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Cadastro CREDE -\n")
    
    print("\nCadastro de CREDE em breve...\n")
    util.timer()

def cadastro_escola():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Cadastro Escola -\n")
    
    print("\nCadastro de Escola em breve...\n")
    util.timer()

#Sessão de entrada para CREDE e Escola, onde os usuários podem acessar o sistema. Atualmente, essas funções estão em desenvolvimento e exibem mensagens de "em breve".
def entrar_crede():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Entrar como CREDE -\n")

    crede.menu_principal()
    
    util.timer()

def entrar_escola():
    util.limpa_tela()
    util.cabecalho()
    print("\n- Entrar como Escola -\n")
    
    escolas.menu_principal()

    util.timer()

escolha_login()