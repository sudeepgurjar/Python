def factorial(x):
	num=1
	if x ==1 or x ==0:
		return num
	else:
		for i in range (1,x+1):
			num= num * i
			
		return num 

#print(factorial(5))