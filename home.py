'''def average (x,y,z):
	average=(x+y+z)/3
	return average
a=int(input ("enter first"))
b=int(input ("enter second:"))
c=int(input ("enter third:"))

d=average(a,b,c)
print(a,b,c,d)'''

choice=int(input("enter no.of term:"))
sum=0
for i in range (choice):
	value=int(input("enter value:"))
	sum=sum+value

average=sum/choice
print("average=",average)