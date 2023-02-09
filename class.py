roll_no = 0
class student:
	def __init__(self):
		self.Name=input("enter a student name: ")
		self.Fathername=input("enter Fathername: ")
		self.age=input("enter age: ")
		self.year=input("enter year: ")
		self.course=input("enter course: ")
		self.contect=input("enter contect: ")
	def show_detail(self):
		print("Name: ",self.name)
		print("Fathername: ",self.Fathername)
		print("age: ",self.age)
		print("year: ",self.year)
		print("course: ",self.course)
		print("contect: ",self.contect)
	def genrate_rollno(self):
		global roll_no
		roll_no=roll_no+1
		self.roll_no=roll_no
		print("Roll_no. of student:",self.roll_no)
print(roll_no)
s1=student()
s1.genrate_rollno()
s1.show_detail()
print(roll_no)
