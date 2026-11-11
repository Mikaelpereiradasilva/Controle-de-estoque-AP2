import crede_fiscalizacao
import util
import escolas
import pathlib

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'


def menu_principal(cnpj_crede_logada):
    util.limpa_tela()
    nome_da_crede = ''
    for crede in escolas.carregar_dados(ARQUIVO_CREDE):
        if crede['cnpj'] == cnpj_crede_logada:
            nome_da_crede = crede['nome']
            break
    while True:
        util.limpa_tela();
        util.cabecalho();
        print(f"Bem-vindo, {nome_da_crede}!\n");
        print("- Menu da CREDE -");
        print("1 - Autorização de Compras");
        print("2 - Fiscalizar Estoques");
        print("0 - Voltar ao menu principal");
        
        opcao = input("Selecione a opção desejada: ")
        
        if opcao == '1':
            autorizacaoCompras()
        elif opcao == '2':
            crede_fiscalizacao.fiscalizar_estoques(cnpj_crede_logada)
        elif opcao == '0':
            break
        else:
            util.opcao_invalida()

def autorizacaoCompras():
    print("em breve");
    util.timer();

