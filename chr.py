
'''num_chr=["0","1","2","3","4","5","6","7","8","9"]

num_count = 0
dot_count=0
other_count=0
user_value=input("enter value:")

for i in user_value:c
    if i in num_chr:
        num_count+=1
    elif i=="." :
        dot_count+=1
    else:
        other_count+=1

if other_count==0 and dot_count==0:
   user_value=int(user_value)
elif other_count==0 and dot_count==1:
   user_value=float(user_value)
else:
    user_value=str(user_value)
print("user_value=",user_value)
print("user_value type=",type(user_value))'''


def typecheck (x):
    
    num_chr=["0","1","2","3","4","5","6","7","8","9"]
    num_count = 0
    dot_count=0
    other_count=0

    for i in x:
        if i in num_chr:
            num_count+=1
        elif i=="." :
            dot_count+=1
        else:
            other_count+=1

    if other_count==0 and dot_count==0:
       x=int(x)
    elif other_count==0 and dot_count==1:
         x=float(x)
    else:
         x=str(x)
    return x

y=input("enter value:")
y=typecheck(y)
print("user given value=",y)
print("type of user given=",type(y))  



