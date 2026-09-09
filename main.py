pizzas = ["Calabresa", "Marguerita", "Frango"]
precos = [40.0, 38.0, 42.0]
print("=== PizzaDev ===")
print("CARDAPIO")
for indice in range(len(pizzas)):
    print(f"{indice + 1} - {pizzas[indice]}: R$ {precos[indice]:.2f}")