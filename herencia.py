#---HERENCIA---
class Human:
	def __init__(self, name, age, sex,):
		self.name=name
		self.age=age
		self.sex=sex

	def speak(self, message):
		print (message, self.name, self.age, self.sex)

class Engineer(Human):
	def work1(self, language):
		print('Im coding in ', language)

class Doctor(Human):
	def work2(self, hospital):
		print('Im working night shift at ', hospital)

class Barista(Human):
	def work3(self, coffee):
		print('Im really good preaping ', coffee)


j = Engineer('John',28,'male')
p = Doctor('Peter', 25,'male')
a = Barista('Alexandra', 30,'female')

j.speak("Hi! Im ")
j.work1("Java")
p.speak("Hi! Im ")
p.work2("Saint Helen Hospital")
a.speak("Hi! Im ")
a.work3("lattes")

