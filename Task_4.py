import random

choices = ['r', 'p', 's']
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    print("\nChoose R(rock), P(paper), or S(scissors):")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please select rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score => You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing! Final Score \n=> You:", user_score, "| Computer:", computer_score)
        break