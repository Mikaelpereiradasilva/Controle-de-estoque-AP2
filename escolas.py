import json
import os
import util
import pathlib

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
        print("4 - Solicitar Autorização de Compra (CREDE)")
        print("0 - Voltar")
        print("="*50)
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            inserirProduto(cnpj_escola_logada)
        elif opcao == '2':
            retiradaDeProduto(cnpj_escola_logada)
        elif opcao == '3':
            consultarEstoque(cnpj_escola_logada)
        elif opcao == '4':
            solicitarAutorizacaoDeCompra(cnpj_escola_logada)
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Por favor, digite um número de 0 a 4.")
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



#FUNÇÕES DE ESTOQUE
def inserirProduto(cnpj_escola_logada):
    estoques = carregar_dados(ARQUIVO_ESTOQUE)
    estoque_da_escola = estoques.setdefault(cnpj_escola_logada, [])
    
    print("\n--- Inserir Novo Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    validade = input("Validade (DD/MM/AAAA): ")
    
    novo_produto = {
        "id": gerar_id(estoque_da_escola),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "validade": validade
    }
    
    estoque_da_escola.append(novo_produto)
    salvar_dados(ARQUIVO_ESTOQUE, estoques)
    print(f"\nProduto '{nome}' inserido com sucesso (ID: {novo_produto['id']})!")
    util.timer()
    util.limpa_tela()

def retiradaDeProduto(cnpj_escola_logada):
    estoques = carregar_dados(ARQUIVO_ESTOQUE)
    retiradas = carregar_dados(ARQUIVO_RETIRADAS)
    estoque_da_escola = estoques.get(cnpj_escola_logada, [])
    retiradas_da_escola = retiradas.setdefault(cnpj_escola_logada, [])


    
    print("\n--- Retirada de Produto ---")
    id_produto = int(input("Informe o ID do produto: "))
    setor_solicitante = input("Setor solicitante (ex: Cantina, Diretoria): ")
    qtd_retirar = int(input("Quantidade solicitada: "))
    
    for produto in estoque_da_escola:
        if produto["id"] == id_produto:
            if produto["quantidade"] >= qtd_retirar:
                produto["quantidade"] -= qtd_retirar
                
                # Para fazer o registro do histórico da movimentação
                registro_retirada = {
                    "id": gerar_id(retiradas_da_escola),
                    "id_produto": produto["id"],
                    "nome_produto": produto["nome"],
                    "setor": setor_solicitante,
                    "quantidade_retirada": qtd_retirar
                }
                
                retiradas_da_escola.append(registro_retirada)
                salvar_dados(ARQUIVO_ESTOQUE, estoques)
                salvar_dados(ARQUIVO_RETIRADAS, retiradas)
                
                print(f"\nRetirada autorizada! {qtd_retirar} unid. de '{produto['nome']}' enviadas para: {setor_solicitante}.")
                util.timer()
                util.limpa_tela()
                return
            else:
                print(f"\nErro: Estoque insuficiente. Quantidade disponível: {produto['quantidade']}")
                util.timer()
                util.limpa_tela()
                return
            
    print("\nErro: Produto não encontrado.")
    util.timer()
    util.limpa_tela()

def consultarEstoque(cnpj_escola_logada):
    estoques = carregar_dados(ARQUIVO_ESTOQUE)
    estoque_da_escola = estoques.get(cnpj_escola_logada, [])

    print("\n--- Estoque Atual ---")
    if not estoque_da_escola:
        print("O estoque está vazio.")
        util.timer()
        util.limpa_tela()
        return

    for p in estoque_da_escola:
        print(f"ID: {p['id']:03d} | Nome: {p['nome']:<15} | Categoria: {p['categoria']:<10} | Qtd: {p['quantidade']:<4} | Validade: {p['validade']}")
    input("\nPressione Enter para voltar ao menu...")
    util.limpa_tela()

def solicitarAutorizacaoDeCompra(cnpj_escola_logada):
    print("\n Em breve")
    util.timer()
    util.limpa_tela()