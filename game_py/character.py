#Clase de personaje modelo
class Character(object):	
	defense = 50
	agility = 25
	hp = 100
	magicAtack = 0
	atack = 0
	atkSpeed = 1
	exp = 0
	
	def __init__(self, name, ocupation):
		self.name = name
		self.ocupation = ocupation	

	def subclassAtack(self):
		if self.ocupation == 'wizard':
			self.magicAtack = self.magicAtack + 70
		elif self.ocupation == 'fighter':
			self.atack = self.atack + 70
	
	def characterStats(self):
		return {"name":self.name, "ocupation":self.ocupation,
			"defense":self.defense, "agility":self.agility,
			"hp":self.hp, "magicAtack": self.magicAtack,
			"atack":self.atack, "atkSpeed":self.atkSpeed,
			"experience":self.exp
		}

