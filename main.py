import seduc
import escolas

def menuPrincipal():
    while True:
        print("=====Usuários=====");
        print("1 - SEDUC.");
        print("2 - Escolas");
        print("0 - Sair");
        
        opcao = input("Selecione o tipo de acesso: ")
        
        if opcao == '1':
            print("\nSistema da SEDUC...\n")
            # seduc.menu_principal()
        elif opcao == '2':
            print("\nSistema Escolar...\n")
            escolas.menu_principal() 
        elif opcao == '0':
            print("\nA encerrar o sistema principal. Até breve!\n")
            break
        else:
            print("\nOpção inválida! Por favor, digite 0, 1 ou 2.\n")

menuPrincipal();