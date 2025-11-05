import random
import time

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors Game")
time.sleep(1)

user_score = 0
computer_score = 0

while True:
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print("Computer is choosing...")
    time.sleep(1)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round.")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Final Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing.")
        break
