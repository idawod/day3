class Person:
	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname

	def __str__(self):
		return "%s %s" %(self.name, self.lastname)

class Student(Person):
	def __init__(self, name, lastname, subject):
		Person.__init__(self, name, lastname)
		self.subject = subject

	def printNameSubject(self):
		print '{} {}, {} ' .format(self.name, self.lastname, self.subject)

	def __str__(self):
		return "%s" %(self.subject)


class Teacher(Person):
	def __init__(self, name, lastname, course):
		Person.__init__(self, name, lastname)
		self.course = course
	def printNameCourse(self):
		print '{} {}, {} ' .format(self.name, self.lastname, self.course)
	def _str_(self):
		return '%s' %(self.course)



