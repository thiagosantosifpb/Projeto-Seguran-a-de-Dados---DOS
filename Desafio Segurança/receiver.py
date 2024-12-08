import random

# Função Diffie-Hellman - Receiver
def diffie_hellman_receiver(P, G):
    if P <= 1:
        raise ValueError("O valor de P deve ser maior que 1.")
    chave_privada_b = random.randint(1, P - 1)
    chave_publica_b = pow(G, chave_privada_b, P)
    
    return chave_privada_b, chave_publica_b

# Função simplificada do DES para criptografar/descriptografar
def criptografar_DES(mensagem_bin, chave_56bits):
    mensagem_int = int(mensagem_bin, 2)
    chave_int = int(chave_56bits, 2)
    resultado_int = mensagem_int ^ chave_int  # Operação XOR entre a mensagem e a chave
    resultado_bin = bin(resultado_int)[2:].zfill(len(mensagem_bin))  # Mantém o mesmo tamanho da mensagem original
    return resultado_bin

# Função de descriptografia DES (mesmo que criptografar, mas aplica a inversa)
def descriptografar_DES(mensagem_criptografada_bin, chave_56bits):
    return criptografar_DES(mensagem_criptografada_bin, chave_56bits)  # DEScriptografar é similar ao DES com subchaves invertidas

# Função para descriptografar a mensagem usando DES
def descriptografar_mensagem_receiver(mensagem_criptografada, chave_secreta):
    chave_56bits = bin(chave_secreta)[2:].zfill(56)[:56]  # Gera a chave de 56 bits a partir da chave secreta
    mensagem_descriptografada = descriptografar_DES(mensagem_criptografada, chave_56bits)  # Descriptografa a mensagem
    # Converte o binário de volta para string
    mensagem_decodificada = ''.join(chr(int(mensagem_descriptografada[i:i+8], 2)) for i in range(0, len(mensagem_descriptografada), 8))
    return mensagem_decodificada

# Definir o número primo n e a base g
P = 23  # Exemplo de número primo
G = 5   # Exemplo de gerador

# Gera as chaves do receiver
chave_privada_b, chave_publica_b = diffie_hellman_receiver(P, G)

# Enviar chave pública para o sender (em um canal inseguro)
print(f"Receiver: Chave pública enviada ao sender: {chave_publica_b}")

# Recebe a chave pública do sender
chave_publica_a = int(input("Receiver: Insira a chave pública recebida do sender: "))

# Cálculo da chave secreta compartilhada
chave_secreta_receiver = pow(chave_publica_a, chave_privada_b, P)

# Recebe a mensagem criptografada do sender
mensagem_criptografada_recebida = input("Receiver: Insira a mensagem criptografada recebida: ")

# Descriptografar a mensagem recebida com DES usando a chave secreta
mensagem_descriptografada = descriptografar_mensagem_receiver(mensagem_criptografada_recebida, chave_secreta_receiver)
print(f"Receiver: Mensagem descriptografada: {mensagem_descriptografada}")
