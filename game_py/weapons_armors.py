
class Item(object):	
	def __init__(self, grade,weight, objct,xitem, xtype): 
		self.grade = grade
		self.weight = weight
		self.objct = objct
		self.pAtack = 0
		self.pCover = 0
		self.xitem = xitem
		
	def subclassStat(self):
		if self.objct == 'armor':
			self.pCover = self.pCover + self.xitem
		elif self.objct == 'weapon':
			self.pAtack = self.pAtack + self.xitem

	def itemStats(self):
		return {"grade":self.grade,"object":self.objct,
			"pAtack":self.pAtack,"pCover":self.pCover
		}

# medium_staf = Item('b',15,'weapon',52,'magical')
# high_staf = Item('a',25,'weapon',70,'magical')
# medium_sword=Item('b',15,'weapon',55,'regular')
# dual_swords=Item('a',25,'weapon',90,'regular')
# medium_robe=Item('b',25,'armor',70,'magical')
# high_robe=Item('a',30,'armor',82,'magical')
# medium_armor =Item('b',25,'armor',80,'regular')
# shield = Item('b',20,'armor',60,'x')
# high_armor =Item('a',30,'armor',120,'regular')
