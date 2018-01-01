# exam1

temp1 = input("string here:")
temp2 = input("char here:")
j = []
m = 0
for i in range(0, len(temp1)):
	n = temp1.find(temp2, m)
	if (n >= 0):
		j.append(n)
		m = n + 1

j = sorted(list(j))
for each in j:
	print(each)
print("数量为：", temp1.count(temp2), end="\n")
