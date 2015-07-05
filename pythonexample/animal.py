class animal(object):
	def __init__(self,type,color):
		self.type='dog'
		self.color=color
	def __str__(self):
		return self.type + '' + self.color
         

