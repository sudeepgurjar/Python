'''length=int (input("enter the length"))
width=int (input ("enter the length"))
area=length*width
print(area)'''


'''def rect_area():
	length=int(input("enter lenght:")) 
	breadth=int (input("enter breadth:"))
	area=length*breadth
	print("area of rectangle=",area)
rect_area()'''


def factorial (x):
	fact=1
	if x==0 or x==1:
		fact=1
	else:
		for i in range (1,x+1):
			fact=fact*i
	return fact
for i in range(4):
	choice=int(input("enter value: "))
	factorial_value=factorial(choice)
	print("factorial of {} is {} ".format(choice,factorial_value))