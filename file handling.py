'''var1=open("intro.txt","a")
var1.write("sudeep gurjar")
var1.close()

var1=open("intro.txt","r")
data=var1.read()
print(data)
var1.close()'''


'''f=open("telephone.txt","a")
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
detail="HI i am {}.\ni am {} year old.\ni live in {}.".format(name,age,city)

print(detail)
f.write(detail)
f.close()

f.close()'''

f=open("telephone.txt","r")
data=f.read()
print(data)
f.close()