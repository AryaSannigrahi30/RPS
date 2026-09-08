import random

print("===== ROCK PAPER SCISSORS =====")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, scissors (or quit): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Draw! 🤝")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win! 🎉")

    else:
        print("Computer Wins! 😄")
        
input("\nPress Enter to exit...")        