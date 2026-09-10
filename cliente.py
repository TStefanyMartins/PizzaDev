cliente = {}

nome = input("Digite seu nome: ")

if not nome:
    print ("Nome inválido")
    exit()
else:    
    telefone = int(input("Digite seu telefone: "))
    if len(str(telefone)) != 11:
        print("Telefone inválido. Deve conter 11 dígitos.")
        exit()

cliente[nome] = telefone

print("Cliente cadastrado com sucesso!")
print(cliente)