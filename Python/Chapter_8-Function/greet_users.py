def greet_users(names):
    """Вывод простого приветствия  для каждого пользователя в списке."""
    for name in names:
        mgs = f"Hello, {name.title()}!"
        print(mgs)

username = ['hannah','try','margot']
greet_users(username)
