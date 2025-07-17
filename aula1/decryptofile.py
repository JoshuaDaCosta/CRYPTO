from cryptography.fernet import Fernet


with open("chave.key", "rb") as key:
    chave=key.read()

fernet = Fernet(chave)

with open("mensagem_cryptografada.txt", "rb") as file:
    dados=file.read()

dados_encryptado=fernet.decrypt(dados)
print(dados_encryptado.decode())

with open("mensagem_decryptografada.txt", "wb") as filed:
    filed.write(dados_encryptado)
print("já está papá")