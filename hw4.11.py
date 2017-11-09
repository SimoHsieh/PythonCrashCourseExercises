favorite_pizzas = ['Mega Meatlover','Butter Chicken' , 'BBQ Meatlover']
favorite_pizzas.insert(0,'Beef')
friend_pizzas =['Mega Meatlover','Butter Chicken' , 'BBQ Meatlover']
friend_pizzas.append('Cheeze')
print('My favorite pizzas are:')
for pizza in favorite_pizzas:
	print(pizza+',')
print("My friend'sfavorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza+',')
