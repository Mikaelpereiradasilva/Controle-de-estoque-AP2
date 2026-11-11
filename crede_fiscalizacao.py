import util
import escolas
import pathlib

pasta_jsons = pathlib.Path(__file__).parent / "Arquivos Json"

ARQUIVO_ESCOLAS = pasta_jsons / 'lista_de_escolas.json'
ARQUIVO_CREDE = pasta_jsons / 'lista_de_credes.json'


def fiscalizar_estoques(cnpj_crede_logada):
    busca_escola = input("Por favor, digite o CNPJ da escola a qual deseja conferir o estoque: ")
    cnpj_escola_buscada = util.padronizar_cnpj(busca_escola)
    
    cnpj_da_crede_da_escola = None
    
    lista_de_escolas = escolas.carregar_dados(ARQUIVO_ESCOLAS)

    for escolas_da_lista in lista_de_escolas:
        if cnpj_escola_buscada == escolas_da_lista['cnpj']:    
                cnpj_da_crede_da_escola = escolas_da_lista['crede']
                break

    if cnpj_da_crede_da_escola is None:
        print("CNPJ da escola não encontrado. Por favor, verifique o CNPJ e tente novamente.")
        util.timer()
        return
    if cnpj_crede_logada != cnpj_da_crede_da_escola:
        print("A escola informada não pertence à CREDE logada. Acesso negado.")
        util.timer()
        return
    else:
        nome_da_escola = ''
        for escola in lista_de_escolas:
            if escola['cnpj'] == cnpj_escola_buscada:
                nome_da_escola = escola['nome']
                break
        util.limpa_tela()
        util.cabecalho()
        print(f"\nEstoque da escola: {nome_da_escola} \nCNPJ: {cnpj_escola_buscada}")
        escolas.consultarEstoque(cnpj_escola_buscada)
        return
