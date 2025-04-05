import random


def guess_the_number():
    
    number = random.randint(1, 100)
    guesses_left = 7
    
    print("Welcome to Guess The Number Game (computer)!")
    print('I am thinking a number between 1 to 100...')

    
    while guesses_left > 0:
        print(f'\n You have {guesses_left} guesses left')
        try:
           guess = int(input('Guess the number: '))
        except ValueError:
            print('Invalid input. Please enter a number')
            continue



        if guess<number :
             print('Too Low Number')
        elif guess > number :
             print('Too High Number')
        else :
             print(f'Congratulations! You got the correct number in {guesses_left} out of 7 guesses')
  

  
        guesses_left -= 1
    if guesses_left == 0:
        print(f'You ran out of tries. The number was {number}')

guess_the_number()        