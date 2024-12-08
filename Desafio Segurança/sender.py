import random

# Função Diffie-Hellman - Sender
def diffie_hellman_sender(P, G):
    if P <= 1:
        raise ValueError("O valor de P deve ser maior que 1.")
    chave_privada_a = random.randint(1, P - 1)
    chave_publica_a = pow(G, chave_privada_a, P)
    
    return chave_privada_a, chave_publica_a

# Função simplificada do DES para criptografar/descriptografar
def criptografar_DES(mensagem_bin, chave_56bits):
    mensagem_int = int(mensagem_bin, 2)
    chave_int = int(chave_56bits, 2)
    resultado_int = mensagem_int ^ chave_int  # Operação XOR entre a mensagem e a chave
    resultado_bin = bin(resultado_int)[2:].zfill(len(mensagem_bin))  # Mantém o mesmo tamanho da mensagem original
    return resultado_bin

# Função para criptografar a mensagem usando DES
def criptografar_mensagem_sender(mensagem, chave_secreta):
    chave_56bits = bin(chave_secreta)[2:].zfill(56)[:56]  # Gera a chave de 56 bits a partir da chave secreta
    mensagem_bin = ''.join(format(ord(c), '08b') for c in mensagem)  # Converte a mensagem de texto para binário
    mensagem_criptografada = criptografar_DES(mensagem_bin, chave_56bits)  # Criptografa a mensagem
    return mensagem_criptografada

# Definir o número primo n e a base g
P = 23  # Exemplo de número primo
G = 5   # Exemplo de gerador

# Gera as chaves do sender
chave_privada_a, chave_publica_a = diffie_hellman_sender(P, G)

# Enviar chave pública para o receiver (em um canal inseguro)
print(f"Sender: Chave pública enviada ao receiver: {chave_publica_a}")

# Recebe a chave pública do receiver
chave_publica_b = int(input("Sender: Insira a chave pública recebida do receiver: "))

# Cálculo da chave secreta compartilhada
chave_secreta_sender = pow(chave_publica_b, chave_privada_a, P)

# Insira a mensagem que deseja criptografar e enviar
mensagem = input("Sender: Insira a mensagem que deseja criptografar e enviar: ")

# Criptografar a mensagem usando DES
mensagem_criptografada = criptografar_mensagem_sender(mensagem, chave_secreta_sender)
print(f"Sender: Mensagem criptografada enviada: {mensagem_criptografada}")
