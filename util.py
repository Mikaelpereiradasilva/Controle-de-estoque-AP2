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

def senha_administrador():
    senha = input("Digite a senha do administrador: ")
    if senha == "1234":
        print("Acesso concedido!")
        timer()
        return True
    else:
        print("Senha incorreta! Acesso negado.")
        timer()
        return False