#Команда break и выход из цикла

promt ='\nPlease enter the name of city you have visited:'
promt += '\nEnter "quit" when you are finished '

while True:
    city = input(promt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


