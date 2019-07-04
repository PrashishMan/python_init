from random import random as r

def flip_coin():
	if r() < 0.5 :
		return "HEADS"
	else: 
		return "TAILS"

print(flip_coin())