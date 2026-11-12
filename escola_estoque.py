import util
import pathlib
import escolas_menus

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESTOQUE = pasta_jsons / 'lista_de_estoques_escolares.json'
ARQUIVO_RETIRADAS = pasta_jsons / 'lista_de_historico_retiradas.json'
ARQUIVO_COMPRAS = pasta_jsons / 'lista_de_solicitacoes_crede.json'
ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'


#FUNÇÕES DE ESTOQUE
def inserirProduto(cnpj_escola_logada):
    estoques = escolas_menus.carregar_dados(ARQUIVO_ESTOQUE)
    estoque_da_escola = estoques.setdefault(cnpj_escola_logada, [])
    
    print("\n--- Inserir Novo Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    validade = input("Validade (DD/MM/AAAA): ")
    
    novo_produto = {
        "id": escolas_menus.gerar_id(estoque_da_escola),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "validade": validade
    }
    
    estoque_da_escola.append(novo_produto)
    escolas_menus.salvar_dados(ARQUIVO_ESTOQUE, estoques)
    print(f"\nProduto '{nome}' inserido com sucesso (ID: {novo_produto['id']})!")
    util.timer()
    util.limpa_tela()

def retiradaDeProduto(cnpj_escola_logada):
    estoques = escolas_menus.carregar_dados(ARQUIVO_ESTOQUE)
    retiradas = escolas_menus.carregar_dados(ARQUIVO_RETIRADAS)
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
                    "id": escolas_menus.gerar_id(retiradas_da_escola),
                    "id_produto": produto["id"],
                    "nome_produto": produto["nome"],
                    "setor": setor_solicitante,
                    "quantidade_retirada": qtd_retirar
                }
                
                retiradas_da_escola.append(registro_retirada)
                escolas_menus.salvar_dados(ARQUIVO_ESTOQUE, estoques)
                escolas_menus.salvar_dados(ARQUIVO_RETIRADAS, retiradas)
                
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
    estoques = escolas_menus.carregar_dados(ARQUIVO_ESTOQUE)
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
