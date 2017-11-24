user_name = ['admin','momo','fafa','bubu','koko']
user_name = []
username = 'admin'
if user_name:
	if username in user_name:
		if username == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print("Hello "+username+" ,thank you for login.")
else:
	print("We need some user")