import util
import pathlib
import escolas_menus

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESTOQUE = pasta_jsons / 'lista_de_estoques_escolares.json'
ARQUIVO_RETIRADAS = pasta_jsons / 'lista_de_historico_retiradas.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'
ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'


def solicitar_autorizacao_compra(cnpj_escola_logada):
    util.limpa_tela()
    
    autorizacoes = escolas_menus.carregar_dados(ARQUIVO_COMPRAS)
    autorizacoes_da_escola = autorizacoes.setdefault(cnpj_escola_logada, [])
    
    print("\n--- Solicitação de Autorização de Compra ---\n")

    ### ESPAÇO PRA DEFINIR A QUANTIDADE DE ORÇAMENTOS DA SOLICITAÇÃO ###
    numero_de_orcamentos = 0
    continuar_no_laco = True
    
    while continuar_no_laco:
        numero_de_orcamentos = input("Informe a quantidade de orçamentos que deseja enviar: ").strip()

        if numero_de_orcamentos.isdigit() == False:
            print("\nEntrada inválida. Por favor, insira um número inteiro.")
            util.timer()
            util.limpa_tela()
            return
    
        if int(numero_de_orcamentos) <= 0:
            continuar = input("\nA quantidade de orçamentos deve ser um número positivo.\nPressione Enter para continuar ou digite 1 para voltar ao menu...").strip()
            if continuar == "1":
                util.limpa_tela()
                return
        if int(numero_de_orcamentos) < 3:
            continuar = input("\nAo enviar menos de 3 orçamentos, você manifesta desinteresse do mercado.\nPressione Enter para continuar ou digite 1 para voltar ao menu... ").strip()
            if continuar == "1":
                util.limpa_tela()
                return
            else:
                numero_de_orcamentos = int(numero_de_orcamentos)
                continuar_no_laco = False
        if int(numero_de_orcamentos) >= 3:
            numero_de_orcamentos = int(numero_de_orcamentos)
            continuar_no_laco = False

    ### ESPAÇO PARA COLETAR OS DADOS DE CADA ORÇAMENTO ###
    lista_de_orçamentos = []
    id_solicitacao = escolas_menus.gerar_id(autorizacoes_da_escola)
    
    util.limpa_tela()
    for i in range(numero_de_orcamentos):
        print(f"--- Orçamento {i + 1} de {numero_de_orcamentos} ---")
        n_orcamento = i+1
        nome_produto = input("Nome do produto: ")
        quantidade = input("Quantidade: ")
        preco = input("Preço Total: ")
        fornecedor = input("Fornecedor: ")
        cnpj_fornecedor = util.padronizar_cnpj(input("CNPJ do Fornecedor: "))

        novo_orcamento = {
            "n_orcamento": n_orcamento,
            "nome_produto": nome_produto,
            "quantidade": quantidade,
            "preco": preco,
            "fornecedor": fornecedor,
            "cnpj_fornecedor": cnpj_fornecedor
        }

        lista_de_orçamentos.append(novo_orcamento)
        deseja_continuar = input("\nDeseja prosseguir com a solicitação? (S/N): ").strip()
        if deseja_continuar == 'n' or deseja_continuar == 'N':
            return
        util.limpa_tela()

    ### ESPAÇO PARA SALVAR A NOVA SOLICITAÇÃO ###
    nova_solicitacao = {
        "id": id_solicitacao,
        "orçamentos": lista_de_orçamentos,
        "situacao": None
    }

    print("RESUMO DA SOLICITAÇÃO DE AUTORIZAÇÃO DE COMPRA")
    for i in lista_de_orçamentos:
        print("="*50)
        print(f"ORÇAMENTO: {i['n_orcamento']}")
        print(f"Nome do Produto: {i['nome_produto']}")
        print(f"Quantidade: {i['quantidade']}")
        print(f"Preço Total: {i['preco']}")
        print(f"Fornecedor: {i['fornecedor']}")
        print(f"CNPJ do Fornecedor: {i['cnpj_fornecedor']}")
    print("="*50)
    confirma_solicitacao = input("\nConfirma o envio da solicitação de autorização de compra? (S/N): ").strip()
    if confirma_solicitacao == 'n' or confirma_solicitacao == 'N':
                print("\nSolicitação cancelada. Retornando ao menu...")
                util.timer()
                return

    autorizacoes_da_escola.append(nova_solicitacao)
    escolas_menus.salvar_dados(ARQUIVO_COMPRAS, autorizacoes)
    print(f"\nSolicitação enviada com sucesso! (ID: {id_solicitacao}) Aguardando análise da CREDE.")
    util.timer()
    util.limpa_tela()

def visualizar_solicitacoes_compra(cnpj_escola_logada):
     print("\n--- Solicitações de Compra (CREDE) ---\n")
     print("Em breve")
     util.timer()
     util.limpa_tela()