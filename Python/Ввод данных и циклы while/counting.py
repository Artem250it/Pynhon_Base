# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# Пользователь решает прервать работу программы

# promt = '\nTell me something, and I will repear it back to you:'
# promt += '\nEnter "quit" to end the program.'
# message = ''
# while message != 'quit':
#     message = input(promt)
#     if message != 'quit':
#         print(message)


#Флаги

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
