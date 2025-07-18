from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization, hashes

# gerar par de chaves publica e privada

chave_priv=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

chave_pub=chave_priv.public_key()

mensagem="Plano B: Lançar o drone furtivo às 3 da madrugada!".encode()


mensagem_cifrada=chave_pub.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

mensagem_decifrada=chave_priv.decrypt(
    mensagem_cifrada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
    
)
print("🔒 Mensagem cifrada:", mensagem_cifrada)
print("🔓 Mensagem decifrada:", mensagem_decifrada.decode())