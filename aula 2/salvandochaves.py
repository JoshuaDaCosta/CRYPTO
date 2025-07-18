from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from assimetrico1 import chave_priv, chave_pub

# Exportar chave privada
with open("chave_privada.pem", "wb") as f:
    f.write(
        chave_priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Exportar chave pública
with open("chave_publica.pem", "wb") as f:
    f.write(
        chave_pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
