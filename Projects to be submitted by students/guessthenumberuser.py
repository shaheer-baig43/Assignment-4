import random

def computer_guess():
    print("Think of a number between 1 and 100, and I'll try to guess it!")


    answer = input('Wanna Play! (Yes/No)')
    if answer.lower() == 'yes':

        low = 1
        high = 100
        attempts = 0
        
        
        while True:
            guess = random.randint(low, high)
            attempts += 1
            print(f"Is it {guess}? (h/l/c)")
            user_feedback = input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if correct: ").lower()
            
            if user_feedback == 'c':
                print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
                break
            elif user_feedback == 'h':
                high = guess - 1
            elif user_feedback == 'l':
                low = guess + 1
            else:
                print("Invalid input. Please enter 'h', 'l', or 'c'.")
                continue

            if attempts > 7 :
                print('I am unable to guess it in 7 attempts. You win!')
    else:
        print('Its ok We will play later!')


computer_guess()
