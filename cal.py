target = int(input())
x = 0


def magicOne(x):
	m = 2 * x + 1
	return m


def magicTwo(x):
	m = 2 * x + 2
	return m


def cal(x):
	string = []
	while True:
		if x == target:
			string = sorted(string)
			out = ""
			for each in string:
				out = out + str(each)
			print(out)
			break
		elif x < target:
			x = magicTwo(x)
			string.append("2")
		elif x > target:
			x = (x - 2 ) / 2
			x = magicOne(x)
			string.pop()
			string.append("1")


cal(x)
