import random as r

options = ["rock", "paper", "sissors"]
computerScore = 0
playerScore = 0

def display_header():
		print(f"Computer Score : {computerScore} Player Score : {playerScore} \n\n")
		print("...rock...")
		print("...paper...")
		print("...sissors...")

def select_winner(player, computer):
	global computerScore
	global playerScore

	if player == computer:
		print(f"It is a tie \n\n\n\n")
		
	elif player == "rock":
		if computer == "paper":
			print(f"Computer beats {player} with {computer} \n\n")
			computerScore+=1
		else:
			print(f"Player beats {computer} with {player} \n\n")
			playerScore+=1

	elif player == "paper":
		if computer == "sissors":
			print(f"Computer beats {player} with {computer} \n\n")
			computerScore+=1
		else:
			print(f"Player beats {computer} with {player} \n\n")
			playerScore+=1

	elif player == "sissors":
		if computer == "rock":
			print(f"Computer beats {player} with {computer} \n\n")
			computerScore+=1
		else:
			print(f"Player beats {computer} with {player} \n\n")
			playerScore+=1

	else:
		print("Something is wrong")


def startGame():
	global computerScore
	global playerScore
	
	bestOf = int(input("Please select the best of :: "))
	while playerScore < bestOf and computerScore < bestOf:
		display_header()
		player = input("Enter your choice player :: ").lower()
		computer = options[r.randint(0,2)]
		select_winner(player, computer)
	
	print_winner()


def print_winner():
	global computerScore
	global playerScore
	if playerScore > computerScore:
		print("Player wins the game")
	else:
		print("Computer wins the game")

	print(f"Computer score :: {computerScore} player score :: {playerScore}")


startGame()