from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open("chave_privada_aula3.pem", "rb") as keyfile:
    chave_piv=serialization.load_pem_private_key(
        keyfile.read(),
        password=None,


    )
mensagem="Itoldyou".encode()
assinatura = chave_piv.sign(
    mensagem,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

#print("mensagem:", mensagem)
#print("assinatura:", assinatura.hex())