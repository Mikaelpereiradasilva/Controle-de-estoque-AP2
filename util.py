import os, time

def cabecalho():
    print("====================================")
    print("= Estoque Escolar unificado - v0.1 =")
    print("====================================")

def limpa_tela():
    os.system("cls")

def timer():
    time.sleep(3)

def opcao_invalida():
    print("\nOpção inválida! Por favor, digite um número válido.\n")
    timer()