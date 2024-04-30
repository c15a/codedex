# Favorite Cities

class Student:
	def __init__(self, name, year, gpa, enrolled):
		self.name = name
		self.year = year
		self.gpa = gpa
		self.enrolled = enrolled

daniel = Student("Daniel li", 10, 4.0, True)
print(vars(daniel))