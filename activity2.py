import random
while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice (["rock", "paper", "scissors"])

    print(f"You choose {user}, Computer choose {computer}")

    if user == computer:
        print("It's a tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "papper" and computer == "rock") or \
         (user == "scissors" and computer == "papper"):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != "y":
        break