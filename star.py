# n=5
# for i in range (1,n+1):
#      print(i*"*")

# n=5
# for i in range(1,n-5):
# 	print(i*"*")

n= int(input("enter value:"))
for i in range(0,n):
	for j in range(0,i+1):
		print("*",end=" ")
	print("\r")    #r=recurence line
	               #n=new line



