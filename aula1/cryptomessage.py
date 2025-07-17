from cryptography.fernet import Fernet
with open("chave.key", "rb") as filekey:
    chave=filekey.read()

fernet=Fernet(chave)
mensagem= "Mensagem é que a chave está segura!".encode()
mensagem_criptografada=fernet.encrypt(mensagem)
print("mensagem criptografada")
print(mensagem_criptografada)
