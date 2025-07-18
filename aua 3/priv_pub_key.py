from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar chave privada (com 2048 bits)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Gerar chave pública a partir da privada
public_key = private_key.public_key()

# Salvar chave privada
with open("chave_privada_aula3.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()  # ou com senha
    ))

# Salvar chave pública
with open("chave_publica_aula3.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
