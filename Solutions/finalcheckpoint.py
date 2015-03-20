import random
import functions

def login(y,usname,password):
	for usr,pswd in y.items():
		if usr==usname:
			if password==pswd:
				return 1
			else:
				return 0
	return 0

def createuser(y):
	print "Enter the username:(atleast 8 characters) "
	username=raw_input()
	if len(username) >= 8:
		print "Password is being created......."
		password=username[3:len(username)]
		password=password+str(random.randint(30,1000))
		print "Your password is "+password
		y[username]=password
	else:
		print "username too short. Try again"
	return


def adddetail(y,us):
	marks=[]
	print "Enter 3 subject marks: "
	for i in range(0,3):
		m=float(raw_input())
		marks.append(m)
	y[us]=marks
	return

def displaystart(student_data):
	if usr in student_data: 
		functions.displaystudents(student_data,usr)
		functions.calcaverage(student_data,usr)
	else:
		adddetail(student_data,usr)
		functions.displaystudents(student_data,usr)
		functions.calcaverage(student_data,usr)
	print "Logging out......"
	return

student_data={}
student_login={}
usr="test"
pwd="test"
flag=0
y=1
while y==1 :
	print "\n1.Login\n2.Register\n3. Exit\nEnter your choice"
	ch=raw_input()
	if ch == "1":
		print "Username: "
		usr=raw_input()
		print "Password: "
		pwd=raw_input()
		flag=login(student_login,usr,pwd)
		if flag == 0:
			print "Not found"
			continue
		else:
			displaystart(student_data)
			continue
	elif ch == "2":
		createuser(student_login)
	elif ch == "3":
		break
	else:
		print "Invalid choice"






