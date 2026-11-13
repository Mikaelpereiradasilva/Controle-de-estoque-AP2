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

def buscar_autorizacoes_crede(cnpj_crede_logada):
    util.limpa_tela()
    
    autorizacoes = escolas_menus.carregar_dados(ARQUIVO_COMPRAS)
    solicitacoes_da_crede = [
        (cnpj_escola, solicitacao)
        for cnpj_escola, solicitacoes in autorizacoes.items()
        for solicitacao in solicitacoes
        if solicitacao.get("cnpj_crede") == cnpj_crede_logada
    ]
    
    print("\n--- Solicitações de Autorização de Compra (CREDE) ---\n")
    
    if not solicitacoes_da_crede:
        print("Não há solicitações de autorização de compra para esta CREDE.")
        util.timer()
        util.limpa_tela()
        return
    
    for i, (cnpj_escola, solicitacao) in enumerate(solicitacoes_da_crede, start=1):
        print(f"Solicitação {i}:")
        print(f"ID da Solicitação: {solicitacao.get('id', 'N/A')}")
        print(f"CNPJ da Escola: {cnpj_escola}")
        print(f"Situação: {solicitacao.get('situacao') or 'Pendente'}")
        print("Orçamentos:")
        for j, orcamento in enumerate(solicitacao.get('orçamentos', []), start=1):
            print(f"  Orçamento {j}:")
            print(f"    Produto: {orcamento.get('nome_produto', 'N/A')}")
            print(f"    Quantidade: {orcamento.get('quantidade', 'N/A')}")
            print(f"    Preço Total: {orcamento.get('preco', 'N/A')}")
            print(f"    Fornecedor: {orcamento.get('fornecedor', 'N/A')}")
            print(f"    CNPJ do Fornecedor: {orcamento.get('cnpj_fornecedor', 'N/A')}")
        print("-" * 40)
    
    input("Pressione Enter para voltar ao menu...")
    util.limpa_tela()
