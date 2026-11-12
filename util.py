import os, time
import hashlib
import secrets
import hmac


#BÁSICO
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



#ADMINISTRADOR PROTEGIDO COM HASH E SALT
def senha_administrador():
    senha = input("Digite a senha do administrador: ")
    salt_adm = '9f87e5fe4387d09a6425aec76291ff25'
    hash_adm = 'd6be2af8b0bb77fb2b3285aaebea68bbd1801ec2cc4de9fb8a57f4775b8f091bc67052d7822baa51d0e80a978a7978fd7a700281d977b5b4f16c50416251846c'

    if verificar_senha(senha, salt_adm, hash_adm):
        print("Acesso concedido!")
        timer()
        return True
    else:
        print("Senha incorreta! Acesso negado.")
        timer()
        return False


#CADASTRO
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