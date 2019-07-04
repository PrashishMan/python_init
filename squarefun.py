def squarefun(num):
	square = num ** 2
	return square

def start():
	count = 0;
	for i in range(1, 20):
		
		s = squarefun(i)
		count += s
		print(f"{i} {s} {count}")

start()