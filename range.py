sum = 0
for oddNum in range(10, 21):
	if oddNum % 2 != 0:
		sum += oddNum
		print("{} added : {}".format(oddNum, sum))

print(sum)