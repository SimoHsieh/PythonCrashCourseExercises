def count_guset(list):
	print("Guest number:"+str(len(list)))

guest_list= ['Bob','Tim','LuLu']
guest_list.insert(0,'BigWhite')
guest_list.insert(2,'FatFat')
guest_list.append('RaRa')

for name in guest_list:
	print("Hi " +name+",I want to invite you to 1/1 dinner.\nSinserely,\nSimo")
print("Sorrt,only two are avaliable.")
count_guset(guest_list)
while True:
	if len(guest_list) >= 3:
		poped_guest = guest_list.pop()
		print(poped_guest +"\tyou are fired.")
		count_guset(guest_list)
	else:
		break
for name in guest_list:
	print("Hi " +name+ ",You are still invited.")
count_guset(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
