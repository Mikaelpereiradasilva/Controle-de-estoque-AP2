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


def aprovar_solicitacao(cnpj_crede_logada):
    autorizacoes = escolas_menus.carregar_dados(ARQUIVO_COMPRAS)
    lista_de_escolas = escolas_menus.carregar_dados(ARQUIVO_ESCOLAS)
    escolas_por_cnpj = {
        escola["cnpj"]: escola
        for escola in lista_de_escolas
        if "cnpj" in escola
    }

    escolas_com_pendencias = {}
    for cnpj_escola, solicitacoes in autorizacoes.items():
        pendentes = [
            solicitacao
            for solicitacao in solicitacoes
            if solicitacao.get("cnpj_crede") == cnpj_crede_logada
            and solicitacao.get("situacao") is None
        ]
        if pendentes:
            escolas_com_pendencias[cnpj_escola] = pendentes

    util.limpa_tela()
    print("\n--- Escolas com Solicitações Pendentes ---\n")
    if not escolas_com_pendencias:
        print("Não há solicitações pendentes para esta CREDE.")
        util.timer()
        return

    for cnpj_escola, pendentes in escolas_com_pendencias.items():
        escola = escolas_por_cnpj.get(cnpj_escola, {})
        nome_escola = escola.get("nome", "Nome não encontrado")
        print(f"Escola: {nome_escola}")
        print(f"CNPJ: {cnpj_escola}")
        print(f"Solicitações pendentes: {len(pendentes)}")
        print("-" * 40)

    busca_escola = input("Digite o CNPJ da escola para analisar as solicitações: ")
    cnpj_escola_buscada = util.padronizar_cnpj(busca_escola)
    if cnpj_escola_buscada is None or cnpj_escola_buscada not in escolas_por_cnpj:
        print("CNPJ da escola não encontrado. Por favor, verifique o CNPJ e tente novamente.")
        util.timer()
        return

    escola = escolas_por_cnpj[cnpj_escola_buscada]
    if escola.get("crede") != cnpj_crede_logada:
        print("A escola informada não pertence à CREDE logada. Acesso negado.")
        util.timer()
        return

    solicitacoes_da_escola = escolas_com_pendencias.get(cnpj_escola_buscada, [])
    if not solicitacoes_da_escola:
        print("Esta escola não possui solicitações pendentes para análise.")
        util.timer()
        return

    print(f"\nSolicitações pendentes de {escola.get('nome', 'Nome não encontrado')}:")
    for solicitacao in solicitacoes_da_escola:
        produtos = ", ".join(
            orcamento.get("nome_produto", "Produto sem nome")
            for orcamento in solicitacao.get("orçamentos", [])
        )
        print(f"ID: {solicitacao.get('id', 'N/A')} - Produtos: {produtos or 'Não informado'}")

    id_digitado = input("Digite o ID da solicitação que deseja analisar: ").strip()
    if not id_digitado.isdigit():
        print("ID inválido. Informe um número.")
        util.timer()
        return

    id_solicitacao = int(id_digitado)
    solicitacao_selecionada = next(
        (
            solicitacao
            for solicitacao in solicitacoes_da_escola
            if solicitacao.get("id") == id_solicitacao
        ),
        None
    )
    if solicitacao_selecionada is None:
        print("Não foi encontrada solicitação pendente com esse ID.")
        util.timer()
        return

    print("\n1 - Aprovar")
    print("2 - Reprovar")
    print("0 - Cancelar")
    decisao = input("Escolha uma opção: ").strip()
    situacoes = {"1": "Aprovada", "2": "Reprovada"}
    if decisao == "0":
        print("Análise cancelada.")
        util.timer()
        return
    if decisao not in situacoes:
        print("Opção inválida. A solicitação não foi alterada.")
        util.timer()
        return

    solicitacao_selecionada["situacao"] = situacoes[decisao]
    escolas_menus.salvar_dados(ARQUIVO_COMPRAS, autorizacoes)
    print(f"Solicitação {id_solicitacao} {situacoes[decisao].lower()} com sucesso.")
    util.timer()

def lista_de_solicitacoes(cnpj_crede_logada):
    util.limpa_tela()
    
    autorizacoes = escolas_menus.carregar_dados(ARQUIVO_COMPRAS)
    escolas = escolas_menus.carregar_dados(ARQUIVO_ESCOLAS)
    nomes_das_escolas = {
        escola["cnpj"]: escola["nome"]
        for escola in escolas
        if "cnpj" in escola and "nome" in escola
    }

    solicitacoes_pendentes = {}
    for cnpj_escola, solicitacoes in autorizacoes.items():
        quantidade_pendente = sum(
            1
            for solicitacao in solicitacoes
            if solicitacao.get("cnpj_crede") == cnpj_crede_logada
            and solicitacao.get("situacao") is None
        )
        if quantidade_pendente:
            solicitacoes_pendentes[cnpj_escola] = quantidade_pendente
    
    print("\n--- Escolas com Solicitações Pendentes (CREDE) ---\n")
    
    if not solicitacoes_pendentes:
        print("Não há escolas com solicitações pendentes para esta CREDE.")
        util.timer()
        util.limpa_tela()
        return
    
    for cnpj_escola, quantidade in solicitacoes_pendentes.items():
        nome_escola = nomes_das_escolas.get(cnpj_escola, "Nome não encontrado")
        print(f"Escola: {nome_escola}")
        print(f"CNPJ: {cnpj_escola}")
        print(f"Solicitações pendentes: {quantidade}")
        print("-" * 40)
    
    input("Pressione Enter para voltar ao menu...")
    util.limpa_tela()