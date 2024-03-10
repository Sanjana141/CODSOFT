import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_choices(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def play_round():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    computer_choice = random.choice(choices)
    
    display_choices(user_choice, computer_choice)
    
    print(determine_winner(user_choice, computer_choice))

def play_game():
    play_round()
    while input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_round()

print("Welcome to Rock-Paper-Scissors!")
play_game()
