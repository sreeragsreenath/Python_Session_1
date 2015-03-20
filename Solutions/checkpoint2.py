a=int(raw_input("Enter the first number  :"))
b=int(raw_input("Enter the second number :"))

opr=raw_input("Enter your option (+, -, *, /, ^): ")

if opr=="+":
	print "a+b="+str(a+b)

elif opr=="-":
	print "a-b="+str(a-b)

elif opr=="*":
	print "a*b="+str(a*b)

elif opr=="/":
	print "a/b="+str(a/b)

elif opr=="^":
	print "a^b"+str(a**b)
else:
	print "Invalid choice"

