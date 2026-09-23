import util

def menu_principal():
    while True:
        util.limpa_tela();
        util.cabecalho();
        print("- Menu da CREDE -");
        print("1 - Autorização de Compras");
        print("2 - Fiscalizar Estoques");
        print("0 - Voltar ao menu principal");
        
        opcao = input("Selecione a opção desejada: ")
        
        if opcao == '1':
            autorizacaoCompras()
        elif opcao == '2':
            fiscalizarEstoques()
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Por favor, digite 0, 1 ou 2.\n")

def autorizacaoCompras():
    print("em breve");
    util.timer();

def fiscalizarEstoques():
    print("em breve");
    util.timer();