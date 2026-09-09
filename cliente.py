cliente = {}

nome = input("Digite seu nome: ")

if not nome.isdigit() and nome.replace(" ", ""):
    print ("Nome inválido")
    
telefone = int(input("Digite seu telefone: "))

cliente[nome] = telefone

print("Cliente cadastrado com sucesso!")


if nome and telefone in cliente.items():
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    
    confirmacao = input("Os dados estão corretos? (S/N): ")
    
    if confirmacao.upper() == "S":
        print("Cadastro confirmado!")
    elif confirmacao.upper() == "N":
        print("Cadastro cancelado.")
        exit()