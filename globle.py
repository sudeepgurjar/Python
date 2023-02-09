def myfunction ():
	global i
	x= int(input("enter a value: "))
	y= int(input("enter a value: "))
	z= x+y 
	print(z)            #being Z a local vairable it cant accessed out side myfunction
	i="I am inside"
	print(id(i))

i="I am fine"
print(id(i)) 
print(i)

myfunction()
print(i)