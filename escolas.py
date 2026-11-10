import json
import os
import util

ARQUIVO_ESTOQUE = 'lista_de_estoques_escolares.json'
ARQUIVO_RETIRADAS = 'lista_de_historico_retiradas.json'
ARQUIVO_COMPRAS = 'lista_de_solicitacoes_crede.json'

def menu_principal():
    util.limpa_tela()
    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE CONTROLE DE ESTOQUE ESCOLAR ")
        print("="*40)
        print("1 - Inserir Novo Produto")
        print("2 - Registrar Retirada de Produto")
        print("3 - Consultar Estoque")
        print("4 - Solicitar Autorização de Compra (SEDUC)")
        print("0 - Voltar")
        print("="*40)
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            inserirProduto()
        elif opcao == '2':
            retiradaDeProduto()
        elif opcao == '3':
            consultarEstoque()
        elif opcao == '4':
            solicitarAutorizacaoDeCompra()
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Por favor, digite um número de 0 a 4.")
            util.timer()
            util.limpa_tela()



def carregar_dados(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_id(dados):
    if not dados:
        return 1
    return max(item["id"] for item in dados) + 1

def inserirProduto():
    estoque = carregar_dados(ARQUIVO_ESTOQUE)
    
    print("\n--- Inserir Novo Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    validade = input("Validade (DD/MM/AAAA): ")
    
    novo_produto = {
        "id": gerar_id(estoque),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "validade": validade
    }
    
    estoque.append(novo_produto)
    salvar_dados(ARQUIVO_ESTOQUE, estoque)
    print(f"\nProduto '{nome}' inserido com sucesso (ID: {novo_produto['id']})!")
    util.timer()
    util.limpa_tela()

def retiradaDeProduto():
    estoque = carregar_dados(ARQUIVO_ESTOQUE)
    retiradas = carregar_dados(ARQUIVO_RETIRADAS)
    
    print("\n--- Retirada de Produto ---")
    id_produto = int(input("Informe o ID do produto: "))
    setor_solicitante = input("Setor solicitante (ex: Cantina, Diretoria): ")
    qtd_retirar = int(input("Quantidade solicitada: "))
    
    for produto in estoque:
        if produto["id"] == id_produto:
            if produto["quantidade"] >= qtd_retirar:
                produto["quantidade"] -= qtd_retirar
                
                # para faze o registro do histórico da movimentação
                registro_retirada = {
                    "id": gerar_id(retiradas),
                    "id_produto": produto["id"],
                    "nome_produto": produto["nome"],
                    "setor": setor_solicitante,
                    "quantidade_retirada": qtd_retirar
                }
                
                retiradas.append(registro_retirada)
                salvar_dados(ARQUIVO_ESTOQUE, estoque)
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

def consultarEstoque():
    estoque = carregar_dados(ARQUIVO_ESTOQUE)
    
    print("\n--- Estoque Atual ---")
    if not estoque:
        print("O estoque está vazio.")
        util.timer()
        util.limpa_tela()
        return
        
    for p in estoque:
        print(f"ID: {p['id']:03d} | Nome: {p['nome']:<15} | Categoria: {p['categoria']:<10} | Qtd: {p['quantidade']:<4} | Validade: {p['validade']}")
        util.timer()
        util.limpa_tela()

def solicitarAutorizacaoDeCompra():
    print("\n Em breve")
    util.timer()
    util.limpa_tela()