a,b=0,1
sum=0
while b<4000000:
	print b
	if b%2 == 0:
		print "it's even!"
		sum = sum+b
	a,b =b,a+b
print 'Sum is',sum	
