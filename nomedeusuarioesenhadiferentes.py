#entradas
nome = input("Digite o nome:  ")
senha = input("Digite a senha: ")
#processamento
while nome == senha:
    print("Senha deve ser diferente do nome. Digite novamente") 
    nome = input("Digite o nome:  ")
    senha = input("Digite a senha: ")