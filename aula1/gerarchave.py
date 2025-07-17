from cryptography.fernet import Fernet


#gerar a chave
chave= Fernet.generate_key()


#salvar no arquivo
with open("chave.key", "wb") as filekey:
    filekey.write(chave)

print("chave gerada !")


