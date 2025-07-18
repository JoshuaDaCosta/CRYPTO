from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from assinaturadigital import *
# Carrega a chave pública
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import serialization

with open("chave_publica_aula3.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

try:
    public_key.verify(
        assinatura,
        mensagem,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Assinatura válida!")
except InvalidSignature:
    print("Assinatura inválida ou mensagem foi alterada.")
