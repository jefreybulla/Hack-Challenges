largestpal=0
x = [0]*1000  #create an array of 100 elements
y = x
for i in range(0,len(x)):  #loop from i= 0 until i=99
  	x[i]=i
	y[i]=i
	#print x 

for j in range(0,len(x)):
	for k in range(0,len(y)):
		pro=x[j]*y[k];
		if pro == reverse_int(pro):
			print 'Palindromic!!'
			if largestpal < pro :
				largestpal = pro
		else:
			print pro
		 
print 'The largest palindromic is' 
print largestpal

def reverse_int(n):
	return int(str(n)[::-1])
