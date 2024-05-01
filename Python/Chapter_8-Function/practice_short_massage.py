def short_massage(name_message,send_messages):
    """ Выводит сообщение"""
    while name_message:
        current_message = name_message.pop()
        print(f"Sending masseges:{current_message}")
        send_messages.append(current_message)

def show_send_message(send_messages):
    """ Отправленные сообщения """
    print("\nThe sended masseges:")
    for sent_m  in send_messages:
        print(sent_m )

name_message = ["Hello","how are you","my name is ","Artsiom","nice to ","meet you"]
send_messages = []

short_massage(name_message[:],send_messages)
show_send_message(send_messages)
print(send_messages)
print(name_message)




# def short_message(name_message, send_messages):
#     """Отправляет сообщения из списка name_message и добавляет их в send_messages."""
#     while name_message:
#         current_message = name_message.pop()  # Извлекаем последнее сообщение из name_message
#         print(f"Отправляется сообщение: {current_message}")
#         send_messages.append(current_message)  # Добавляем сообщение в список send_messages

# def show_sent_messages(send_messages):
#     """Выводит список отправленных сообщений из send_messages."""
#     print("\nОтправленные сообщения:")
#     for sent_message in send_messages:
#         print(sent_message)

# # Список сообщений для отправки
# name_message = ["Hello", "how are you", "my name is", "Artsiom", "nice to", "meet you"]
# send_messages = []

# # Вызываем функцию short_message для отправки сообщений
# short_message(name_message, send_messages)

# # Выводим список отправленных сообщений с помощью функции show_sent_messages
# show_sent_messages(send_messages)
