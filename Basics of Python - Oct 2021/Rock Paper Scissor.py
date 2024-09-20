import random
while True:
    options = ["rock", "paper", "scissor"]
    computer= random.choice(options)
    choice=input("Enter your Choice - Rock/Paper/Scissor :").lower()

    if choice == "rock" and computer == "scissor":
        print("You win! Computer chose - ",computer)
    elif choice == "rock" and computer == "paper":
        print("Computer wins! Computer chose - ",computer)
    elif choice == "paper" and computer == "rock":
        print("You win! Computer chose - ",computer)
    elif choice == "paper" and computer == "scissor":
        print("Computer wins! Computer chose - ",computer)
    elif choice == "scissor" and computer == "paper":
        print("You win! Computer chose - ",computer)
    elif choice == "scissor" and computer == "rock":
        print("Computer wins! Computer chose - ",computer)
    elif choice == computer:
        print("Its a draw")
    