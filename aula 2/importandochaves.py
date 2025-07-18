from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
# Ler chave privada do arquivo
with open("chave_privada.pem", "rb") as f:
    chave_privada = serialization.load_pem_private_key(
        f.read(),
        password=None,  # ou coloca a senha se estiver encriptada
        backend=default_backend()
    )

# Ler chave pública do arquivo
with open("chave_publica.pem", "rb") as f:
    chave_publica = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

print("chave privida: ", chave_privada)
print("chave publica: ", chave_publica)