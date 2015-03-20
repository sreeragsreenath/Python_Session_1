#Build your story game


def ending1(name):
	print name+" has reached safely in the village. But he doesnt like the place so he goes back"
	return

def ending2(name,weapon):
	print name+" rented a house and was staying peacefully. Once day, he was surprised to find Darth Vader and Loki attack him. So he fought them off with his mystical "+weapon
	return

def ending3(name,money):
	print name+" was waiting for the bus when he pocket got picket and he lost a total of "+str(money)+" Pesos"
	return

print "Enter your name: "

name=raw_input()

print "Once upon a time, "+name+" was going to a new village filled with awesome creatures and many quests.\nOn the way he see three roads"

ta="y"
while ta=="y":
	print "\nWhich one should he choose?\n1.Road1 \n2.Road2 \n3.Road3"
	choice=int(raw_input("Enter the road to take: "))
	if choice == 1:
		ending1(name)
	elif choice == 2: 
		print "You may need a weapon for this one: "
		weapon= raw_input()
		ending2(name,weapon)
	elif choice == 3: 
		print "Well how much money do you have? "
		money=float(raw_input())
		ending3(name,money)
	else:
		print "So there is no way like that Try again"
	print "\nDo you want to try again?(y/n):  "
	ta= raw_input()
