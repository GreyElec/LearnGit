class C:
	def __getattribute__(self, name):
		print("getattribute")
		return super().__getattribute__(name)

	def __setattr__(self, name, value):
		print("setattar")
		return super().__setattr__(name, value)

	def __delattr__(self, name):
		print("delattar")
		return super().__delattr__(name)

	def __getattr__(self, item):
		print("getattar")


c = C()
c.x = 1
del c.x
