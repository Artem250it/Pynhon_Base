# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print('My favorite foods are:')
# print(my_foods)

# print("\nMyfriend's favorite foods are:")
# print(friend_foods)

pizza_my = ['Neapolitan Pizza','Pepperoni Picasso','Supreme Symphony','Veggie Victory']
pizza_my.append('Pepperoni HOT')
friend_pizza = pizza_my[:]



friend_pizza.list.append('Thiladelfia')
friend_pizza.append('Kola')

#
print(pizza_my)
print('My favorite pizzas are:')
for my in pizza_my[:1]:

 print(my)

print(friend_pizza)


print("\nMy friend/s favorite pizzas are:")
for friend in friend_pizza[1:2]:
 print(friend)