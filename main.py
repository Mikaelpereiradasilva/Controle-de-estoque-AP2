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

menuPrincipal();
