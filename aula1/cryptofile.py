from cryptography.fernet import Fernet
with open("chave.key", "rb") as key:
    chave=key.read()

fernet = Fernet(chave)

with open("mensagem.txt", "rb") as file:
    dados=file.read()

dados_encryptado=fernet.encrypt(dados)
print(dados_encryptado)

with open("mensagem_cryptografada.txt", "wb") as filed:
    filed.write(dados_encryptado)
print("já está papá")