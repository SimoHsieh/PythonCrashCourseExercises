river = {
	'egypt': 'nile',
	'river1': 'country1',
	'river2': 'country2',
	'river3': 'country3',
	'river4': 'country4',
	}
for key, value in sorted (river.items()):
	print("The " + key.title() + "runs through "+value+".")
for key in sorted(river.keys()):
	print(key)
for value in sorted(river.values()):
	print(value)
