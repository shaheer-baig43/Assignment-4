import random

print("This is a simple rock, paper, and scissors game.")


choices = ['rock', 'paper', 'scissors']

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(choices)
print(f"This is my choice: {computer_choice}")
if player_choice == computer_choice:
    print(f"Both players selected {player_choice}. It's a tie!")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print("Rock smashes scissors! You win!")
elif player_choice == 'paper' and computer_choice == 'rock':
    print("Paper covers rock! You win!")
elif player_choice == 'scissors' and computer_choice == 'paper':
    print("Scissors cuts paper! You win!")
elif player_choice == 'rock' and computer_choice == 'paper':
    print("Paper covers rock! I win!")
elif player_choice == 'paper' and computer_choice == 'scissors':
    print("Scissors cuts paper! I win!")
elif player_choice == 'scissors' and computer_choice == 'rock':
    print("Rock smashes scissors! I win!")
else:
    print("Invalid input")

