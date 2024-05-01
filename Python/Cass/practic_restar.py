class Restaurant():
    """Назвиние  и тип кухни  ресторана"""

    def __init__(self,restaurant_name,cuisine_type) -> None:
        """Инициализирует атрибуты restaurant_name и cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Описания ресторана"""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"Restaurant type of cuisine {self.cuisine_type}.")

    def open_restaurant(self):
        """Выводит сообщение что ресторан открыт. """
        print(f"The {self.restaurant_name} is open.")

restaurant_pitzza_hut = Restaurant("Pitzza HUT","Italian")
restaurant_ham = Restaurant('HAM','Indian')
restaurant_cook = Restaurant('COOK','Franch')
# print(f"Restaurant name {restaurant_pitzza_hut.restaurant_name}.")
# print(f"It has {restaurant_pitzza_hut.cuisine_type} cuisine.")
restaurant_pitzza_hut.describe_restaurant()

# print(f"\nRestaurant name {restaurant_ham.restaurant_name}.")
# print(f"It has {restaurant_ham.cuisine_type} cuisine.")
restaurant_ham.describe_restaurant()

restaurant_cook.describe_restaurant()