# # Список моделей которые нужно напечатать.
# unprinted_desing = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# # Цикл последовательнопечатает каждую модель до конца списка .
# # После печати каждая модель перемещается в список completed_models.
# while unprinted_desing:
#     current_desing = unprinted_desing.pop()
#     print(f"Printing model: {current_desing}")
#     completed_models.append(current_desing)
# # Вывод всех готовых моделей.
# print("\nThe following models have been printed:")
# for complited_model in completed_models:
#     print(complited_model)
    #________________________________________________________________________________

def printing_models(unprinted_desing, complited_models):
    """Имитирует печать моделей, пока список не станет пустым.
       Каждая модель после печати перемещается в completed_models."""
    while unprinted_desing:
        current_desing = unprinted_desing.pop()
        print(f"Printed model : {current_desing}")
        complited_models.append(current_desing)

def show_copmleted_models(complited_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for complited_model in complited_models:
        print(complited_model)
