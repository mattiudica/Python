class Mate(object):
	def __init__(self,yerba,extra,temp):
		self.yerba=yerba
		self.extra=extra
		self.temp=temp

	def cebarMate(self):
		if self.yerba=='amarga'and\
		   self.extra=='cafe'and\
		   self.temp in range(70,81):
			print('Buen mate')
		else:
			print('Mate feo')




miMate = Mate('amarga','cafe',100)
miMate.cebarMate()


