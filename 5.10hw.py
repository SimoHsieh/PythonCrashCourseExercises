current_user = ['admin','momo','fafa','bubu','koko','John']
new_user = ['momo','fafa','fatfat','bigwhite','lulu','JOHN']
current_user_lower = []
for name in current_user:
	current_user_lower.append(name.lower())
for name in new_user:
	if name.lower() in current_user_lower:
		print("Name "+name+" is used,need to enter a new username.")
	else:
		print("Username "+name+" is available.")