#---CLASES Y OBJETOS---
hello = 'Hi my name is '

class Human:
	def __init__(self, name, age, sex, job):
		self.name=name
		self.age=age
		self.sex=sex
		self.job=job

	def speak(self, message):
		print (hello, self.name, self.age, self.sex, self.job)

j = Human('John',28,'male','engineer')
p = Human('Peter', 25,'male','barista')
a = Human('Alexandra', 30,'female','doctor')

j.speak("check")
p.speak("check")
a.speak("check")
