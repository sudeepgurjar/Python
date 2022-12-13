#dictionary,(key,value,pair)
dict1={"name":"sudeep","class":"BCA","subject":"maths"}
print(dict1)

'''for i in dict1:
	print(i)
	print(dict1[i])'''

'''for i,j in dict1.items():
		print(i)
		print(j)'''

 #update
dict2={1:"23",2:"25",5:"26"}
for i,j in dict2.items():
	print(i)
	print(j)		
		
#add new key						
dict1["name"]="sudeep"
print(dict1)
dict1["school"]="mrsc"
print(dict1)

#pop
dict1.pop("school")
print(dict1)