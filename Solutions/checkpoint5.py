def addstudents():
	print "Insert the number of students: "
	n=int(raw_input())
	y={}
	marks=[]
	for i in range(0,n):
		print "Enter the name: "
		name=raw_input()
		print "Enter 3 subject marks: "
		for j in range(0,3):
			mark=float(raw_input())
			marks.append(mark)
		y[name]=marks
		marks=[]
	return y

def displaystudents(y):
	for nm,mks in y.items():
		print "Name: {} \nMarks: {}".format(nm,mks)
	return


def calcaverage(y):
	average={}
	for nm,mks in y.items():
		total=0
		for i in mks:
			total=total+i
		average[nm]=float(total/len(mks))

	for nm,avg in average.items():
		print "Name: {} \nAverage: {}".format(nm,avg)
	return

def calctotal(y):
	totalm={}
	for nm,mks in y.items():
		total=0
		for i in mks:
			total=total+i
		totalm[nm]=total
	for nm,ttl in totalm.items():
		print "Name: {} \nSum: {}".format(nm,ttl)
	return

student_data=addstudents()
tn="y"
while tn == "y":
	print "\n1.Print all the records\n2.Print the average marks \n3 Print the total marks\nEnter your choice: "
	ch=raw_input()
	if ch=="1":
		displaystudents(student_data)
	elif ch=="2":
		calcaverage(student_data)
	elif ch=="3":
		calctotal(student_data)
	else:
		print "Invalid choice"
	print "Want to continue? (y/n): "
	tn=raw_input()



