cliente = {}

nome = input("Digite seu nome: ")

if not nome.isdigit() and nome.replace(" ", ""):
    print ("Nome inválido")
    
telefone = int(input("Digite seu telefone: "))

cliente[nome] = telefone

print("Cliente cadastrado com sucesso!")