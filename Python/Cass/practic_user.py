class User():
    """Описание пользователя."""
    def __init__(self,first_name,last_name,age,interests):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.interests = interests

    def describe_user(self):
        print(f"\nName is - {self.first_name}")
        print(f"Last nane is - {self.last_name}")
        print(f"Age is - {self.age}")
        print(f"interest - {self.interests}")

    def greet_users(self):
        print(f"Hello {self.first_name}")


piter = User("Piter","Parker","25","SpiderMan")
piter.greet_users()
piter.describe_user()

doris = User("Doris","Mantana","30","Cars")
doris.greet_users()
doris.describe_user()