#Project 5: Hangman Game


import random


words = ['shaheer', 'game', 'mango', 'python']



word = random.choice(words)
guess_letters = []

attempts = 6

print('This is a hangman game!')
print('_' * len(word))


while attempts > 0 :
    guess = input('\n  Enter your guessed letter: ').lower()
    if len(guess) != 1  :
        print('Write one alphabet only')
    elif not guess.isalpha():
        print('Write a letter only')
        continue
    if guess in guess_letters :
        print('You already guessed this letter')
        continue
    guess_letters.append(guess)
    if guess not in word :
        print('Wrong guess')
        attempts -= 1
        print(f'You have {attempts} attempts left')
    else:
        print('Good guess')
    
    displayed_word = " ".join(letter if letter in guess_letters else "_" for letter in word)
    print(displayed_word)

    if "_" not in displayed_word :
         print(f'Congratulations! the correct word is {word}')
         break
else : 
    print(f'Game Over! the correct word is {word}')
           