#import simple
#import simple1 as s 
from simple1 import factorial
# calculating permutation


n,r =int(input("enter value:")), int(input("enter value of R:"))
if n > r:
	result= factorial(n)/(factorial(n-r))
	print(result)
else:
	print("can not compute")
	comb =(factorial(n)) / (factorial(r)) / (factorial(n-r))
	print("comb",comb)