from cryptography.fernet import Fernet
from cryptomessage import mensagem_criptografada

with open("chave.key", "rb") as filekey:
    chave=filekey.read()
fernet=Fernet(chave)

mensagem_original=fernet.decrypt(mensagem_criptografada)
print(mensagem_original.decode())