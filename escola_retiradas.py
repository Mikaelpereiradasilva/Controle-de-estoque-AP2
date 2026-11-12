import escolas_menus
import util
import pathlib

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESTOQUE = pasta_jsons / 'lista_de_estoques_escolares.json'
ARQUIVO_RETIRADAS = pasta_jsons / 'lista_de_historico_retiradas.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'
ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'


def visualizar_historico_retiradas(cnpj_escola_logada):
    retiradas = escolas_menus.carregar_dados(ARQUIVO_RETIRADAS)
    retiradas_da_escola = retiradas.get(cnpj_escola_logada, [])

    print("\n--- Histórico de Retiradas ---")
    if not retiradas_da_escola:
        print("Não há registros de retiradas.")
        util.timer()
        util.limpa_tela()
        return

    for r in retiradas_da_escola:
        print(f"ID Retirada: {r['id']:03d} | ID Produto: {r['id_produto']:03d} | Nome Produto: {r['nome_produto']:<15} | Setor: {r['setor']:<10} | Quantidade Retirada: {r['quantidade_retirada']}")
    input("\nPressione Enter para voltar ao menu...")
    util.limpa_tela()