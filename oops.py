#oops concepts

# 1. class and object
# 2. data abstraction
# 3. polymorphism
# 4. inheritance
# 5. data encapsulation
# 6. dynamic biuding



# class student:
# 	def __init__(self,name,course,subject):
# 		self.name=name
# 		self.course=course
# 		self.subject=subject

# 	def show(self):
# 		print("Name:",self.name)
# 		print("Course:",self.course)
# 		print("Subject:",self.subject)


# S1=student("Raam","BCA","ADA")
# S1.show()


#user input

class student:
	def __init__(self):
		self.name=input ("enter name:")
		self.course=input("enter course:")
		self.subject=input ("enter subject:")

	def show(self):
		print("Name:",self.name)
		print("Course:",self.course)
		print("Subject:",self.subject)



S1=student()
S1.show()
S2=student()
S2.show()

