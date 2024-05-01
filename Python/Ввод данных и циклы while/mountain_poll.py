responses= {}

polling_active = True
while polling_active:
    name = input('\nWhat is your name? ')
    responce = input('Which mountain wold you like clibb someday? ')

    responses[name] = responce

    repeat = input('Would you like to let another person respond (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\n---PollResults---')
for name , responce in responses.items():
    print(f"{name} would like to climb {responce}.")