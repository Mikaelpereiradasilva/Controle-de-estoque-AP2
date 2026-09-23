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
            util.opcao_invalida()

def autorizacaoCompras():
    print("em breve");
    util.timer();

def fiscalizarEstoques():
    Buscaescola = input("Por favor, digite o CNPJ da escola a qual deseja conferir o estoque")
    #código para buscar o cnpj(só pode ser feito após ter sido feito o código de cadastro)
    for i in CNPJ:
        if Buscaescola == CNPJ[i]:
            util.limpa_tela();
            print(estoque[i])
            util.timer();
            break
    while True:
        opcao = input("\nQuando quiser retornar ao Menu Crede, pressione 1.\n")
        if opcao == 1:
            menu_principal()
        else:
            print("\nOpção inválida! Por favor, digite 1 para voltar ao Menu Crede.\n")

    util.timer();
