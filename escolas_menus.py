import json
import os
import util
import pathlib
import escola_estoque, escola_retiradas, escola_autorizacao

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESTOQUE = pasta_jsons / 'lista_de_estoques_escolares.json'
ARQUIVO_RETIRADAS = pasta_jsons / 'lista_de_historico_retiradas.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'
ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'


#PRINCIPAL
def menu_principal(cnpj_escola_logada):
    util.limpa_tela()
    nome_da_escola = ''
    for escola in carregar_dados(ARQUIVO_ESCOLAS):
        if escola['cnpj'] == cnpj_escola_logada:
            nome_da_escola = escola['nome']
            break
    for crede in carregar_dados(ARQUIVO_CREDE):
        if crede['cnpj'] == escola['crede']:
            nome_da_crede = crede['nome']
            break
    while True:
        print("\n" + "="*50)
        print("==    SISTEMA DE CONTROLE DE ESTOQUE ESCOLAR    ==")
        print("="*50)
        print("Bem-vindo(a) à Escola com CNPJ: ", cnpj_escola_logada)
        print(nome_da_escola, "-", nome_da_crede)
        print("\nEscolha uma opção:")
        print("1 - Inserir Novo Produto")
        print("2 - Registrar Retirada de Produto")
        print("3 - Consultar Estoque")
        print("4 - Visualizar Histórico de Retiradas")
        print("5 - Solicitar Autorização de Compra (CREDE)")
        print("0 - Voltar")
        print("="*50)
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            escola_estoque.inserirProduto(cnpj_escola_logada)
        elif opcao == '2':
            escola_estoque.retiradaDeProduto(cnpj_escola_logada)
        elif opcao == '3':
            escola_estoque.consultarEstoque(cnpj_escola_logada)
        elif opcao == '4':
            escola_retiradas.visualizar_historico_retiradas(cnpj_escola_logada)
        elif opcao == '5':
            escola_autorizacao.solicitarAutorizacaoDeCompra(cnpj_escola_logada)
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Por favor, digite um número de 0 a 5.")
            util.timer()
            util.limpa_tela()



#BÁSICO
def carregar_dados(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return {}
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_id(dados):
    if not dados:
        return 1
    return max(item["id"] for item in dados) + 1




