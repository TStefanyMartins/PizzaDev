cliente = {}

nome = input("Digite seu nome: ")

if not nome:
    print ("Nome inválido")
    exit()
else:    
    telefone = int(input("Digite seu telefone: "))

cliente[nome] = telefone

print("Cliente cadastrado com sucesso!")
