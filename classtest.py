class test:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def setdata(self,a,b):
		self.a = a
		self.b = b
	def calculate(self):
		print(bin(self.a^self.b).count('1'))

a = test(16,255)
a.calculate()
a.setdata(1,8)
a.calculate()