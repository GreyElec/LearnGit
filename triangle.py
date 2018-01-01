s = sorted(input().split())
a = []
for each in s:
	each = int(each)
	a.append(each)
s = a
if s[3] > s[2] - s[1] & s[3] < s[2] + s[1]:
	print("triangle")
else:
	n = 3
	for i in range(3):
		for j in range(i + 1, 3):
			if s[i] + s[j] == s[n]:
				print("segment")
			elif n > i & n > j:
				m -= 1
			else:
				break
	print("impossible")
