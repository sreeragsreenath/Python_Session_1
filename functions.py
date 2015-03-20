def displaystudents(y,us):
	print "Name: {} \nMarks: {}".format(us,y[us])
	return


def calcaverage(y,us):
	total=0
	for i in y[us]:
		total=total+i
	average=float(total/len(y[us]))
	print "Name: {} \nAverage: {}".format(us,average)
	return
