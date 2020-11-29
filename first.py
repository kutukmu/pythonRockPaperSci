import random
choices = ["rock" ,"paper", "scissors"]
randnum  = random.randint(0,2)
player1 = input("Plase enter your choice: ")
player2 = choices [randnum]

print("Player 2 choice: " + player2)


if player1 == player2:
    print("Draw")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 Win")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 win")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 win")
else:
    print("player 2 win")