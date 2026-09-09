pizzas = ["Calabresa", "Marguerita", "Frango"]
precos = [40.0, 38.0, 42.0]
print("=== PizzaDev ===")
print("CARDAPIO")
for indice in range(len(pizzas)):
    print(f"{indice + 1} - {pizzas[indice]}: R$ {precos[indice]:.2f}")
    
opcao = input("Escolha o numero da pizza: ")
if opcao.isdigit() and 1 <= int(opcao) <= len(pizzas):
    indice = int(opcao) - 1
    print(f"Pizza escolhida: {pizzas[indice]}")
    print(f"Preco unitario: R$ {precos[indice]:.2f}")
else:
    print("Opcao invalida.")