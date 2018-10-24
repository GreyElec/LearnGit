class Potato:
	def hello(self):
		print('calling on method in Potato')


class Child(Potato):
	pass


child = Child()
child.hello()
