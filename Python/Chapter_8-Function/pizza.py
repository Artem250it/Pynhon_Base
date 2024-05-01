def make_pizza(size, *toppings):
    """Вывод списка заказанных топпингов."""
    print(f"\nMaking a {size}-inh pizza with the following toppings:")
    for topping in toppings :
        print(f"- {topping.title()}")


