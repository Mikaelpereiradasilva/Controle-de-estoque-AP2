import os, time
import hashlib
import secrets
import hmac

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
def padronizar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return None
    else:
        return cnpj

# Função para gerar hash da senha com salt
def gerar_hash_senha(senha):
    salt = secrets.token_bytes(16)

    senha_hash = hashlib.scrypt(
        senha.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return salt.hex(), senha_hash.hex()

# Função para verificar a senha digitada com o hash e salt armazenados
def verificar_senha(senha_digitada, salt_hex, hash_armazenado):
    salt = bytes.fromhex(salt_hex)

    hash_calculado = hashlib.scrypt(
        senha_digitada.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    ).hex()

    return hmac.compare_digest(hash_calculado, hash_armazenado)