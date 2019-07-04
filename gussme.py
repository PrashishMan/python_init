import random as r

playagain = True
while playagain:
	a = r.randint(0, 10);
	b = int(input("please guess the number::  "))

	while b != a:
		if b > a:
			b = int(input("Sorry your guess is higher!\n Try Again::  "))
		elif a > b:
			b = int(input("Sorry your guess is lower!\n Try Again::  "))

	print(f"Congtulation you have sucessfully figured out the number : {b} ")
	
	again = input("Do you want to play again? (Y/N) :: ")
	if again == "Y" or again == "y":
		playagain = True
	elif again == "N" or again == "n":
		playagain = False
	else:
		playagain = False
