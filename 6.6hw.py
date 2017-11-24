favorite_languages = {
	'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
poll_name = [
	'jen', 'sarah', 'edward', 'phil', 'simo', 'bigwhite',		
]
for name in poll_name:
	if name in favorite_languages.keys():
		print(name.title()+" you already voted,thank you for your responding.")
	else:
		print(name.title()+" I will like to invite you to to take the poll.")