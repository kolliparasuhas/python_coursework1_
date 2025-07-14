import random

def get_user_choice():
    print("Enter your choice (rock, paper, or scissors or 'exit' to quit):")
    return input().lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Game loop
while True:
    user_choice = get_user_choice()
    if user_choice == "exit":
        print("Game Over!")
        break
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue
    else:
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")
