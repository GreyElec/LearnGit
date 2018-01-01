weight = int(input())
if weight <= 10:
	print("3.50")
else:
	n = weight - 10
	p1 = 0.75 * n
	pt = p1 + 3.50
	print(pt)

