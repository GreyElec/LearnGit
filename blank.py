
A = input().split(",")
A.pop(0)
for each in A:
	if int(each) % 4 == 0:
		print("True")
		break
	else:
		print("False")
		break
