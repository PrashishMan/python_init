response = None
num = [1,2,3,4,4,4,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]

num2.clear()
print(num2)

num.append(11)
num.extend(range(12, 21))
num.insert(2, 2.5)

num.remove(4)     

num.insert(len(num), "Last")
item1 = num.pop(2)
# item2 = num.pop(4)
# item3 = num.pop(5)

while response != 'please':
	response = input("Please say please :: ").lower();
	print(item1)
	# print(item2)
	# print(item3)
	print("..................\n\n\n")


count = 0
while count < len(num) and count <= 100:
	print(num[count])
	count += 1