class employee:
	def __init__(self):
		self.name=input("Name of the employee:")
		self.employee_Id=input("employee Id:")
		self.contect=input("contect no.:")
		self.addres=input("addres:")
		self.department=input("department name:")
	def show_detail(self):
		print("employee id :",self.employee_Id)
		print("Name:",self.name)
		print("addres:",self.addres)
		print("contect:",self.contect)
	def dwrite(self):
		f=open("employee.txt","a")
		data=self.employee_Id+","+self.name+","+self.contect+","+self.addres+","+self.department+"\n"
		f.write(data)
		print("data entried successfuly")

class Manager(employee):
	#employee().__init__()
	def dept_employee_detail(self):
		f=open("employee.txt","r")
		data=f.read()
		data_row = data.split("\n")
		data_row.pop()
		valid_row=[]
		for i in data_row:
			x=i.split(",")
			if self.department==x[len(x)-1]:
				valid_row.append(i)

class owner(Manager,employee):
	def show_all(self):
		f=open("employee.txt","r")
		data=f.read()
		data_row=data.split("\n")
		data_row.pop()
		for i in data_row:
			x=i.split(",")
			print("--------------------")
			#print("------")
			print("employee Id:",x[0])
			print("Name:",x[1])
			print("contect:",x[2])
			print("addres:",x[3])
			print("department:",x[4])
		print("----------------------------")
			
s1=employee()
s2=Manager()
s3=owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()
s1.show_detail()
s2.show_detail()
s2.dept_employee_detail()
s3.show_detail()
s3.dept_employee_detail()
s3.show_all()










