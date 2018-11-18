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

class Unemployed(Barista, Doctor):
	pass

h = Unemployed('Hellen', 35, 'trans')

h.speak('Hi! Im ')
h.work3('nothing')
h.work2('none')
