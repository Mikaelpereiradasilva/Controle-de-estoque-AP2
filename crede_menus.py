import crede_fiscalizacao
import crede_autorizacao
import util
import escolas_menus
import pathlib


pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'


def contar_solicitacoes_pendentes(cnpj_crede):
    autorizacoes = escolas_menus.carregar_dados(ARQUIVO_COMPRAS)
    return sum(
        1
        for solicitacoes in autorizacoes.values()
        for solicitacao in solicitacoes
        if solicitacao.get("cnpj_crede") == cnpj_crede
        and solicitacao.get("situacao") is None
    )


def menu_principal(cnpj_crede_logada):
    util.limpa_tela()
    nome_da_crede = ''
    for crede in escolas_menus.carregar_dados(ARQUIVO_CREDE):
        if crede['cnpj'] == cnpj_crede_logada:
            nome_da_crede = crede['nome']
            break
    while True:
        util.limpa_tela();
        util.cabecalho();
        print(f"Bem-vindo, {nome_da_crede}!\n");
        quantidade_pendente = contar_solicitacoes_pendentes(cnpj_crede_logada)
        print(f"Solicitações pendentes: {quantidade_pendente}\n")
        print("- Menu da CREDE -");
        print("1 - Autorização de Compras");
        print("2 - Fiscalizar Estoques");
        print("3 - Aprovar/Reprovar Solicitações");
        print("0 - Voltar ao menu principal");
        
        opcao = input("Selecione a opção desejada: ")
        
        if opcao == '1':
            crede_autorizacao.buscar_autorizacoes_crede(cnpj_crede_logada)
        elif opcao == '2':
            crede_fiscalizacao.fiscalizar_estoques(cnpj_crede_logada)
        elif opcao == '3':
            crede_autorizacao.aprovar_solicitacao(cnpj_crede_logada)
        elif opcao == '0':
            break
        else:
            util.opcao_invalida()

def autorizacaoCompras():
    print("em breve");
    util.timer();
