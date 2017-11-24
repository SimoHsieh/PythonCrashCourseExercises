cities = {
	'city1': {
		'country':'country1',
		'population':'1341',
		'fact':'fact1',
		},
	'city2': {
		'country':'country2',
		'population':'1467',
		'fact':'fact2',
		},
	'city3': {
		'country':'country3',
		'population':'16536',
		'fact':'fact3',
		},
}
for key ,value in sorted(cities.items()):
	print(key)
	for key ,value in value.items():
		print(key+":"+value)

