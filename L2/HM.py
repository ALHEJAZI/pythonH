import random

words = ["apple", "banana", "cherry", "dog", "cat", "horse"]


word = random.choice(words)


guesses = []
lives = 3

while lives > 0:

    
    print("You have", lives, "lives left.")
    print("You have guessed the following letters:", guesses)
    print("The word is:", "_" * len(word))

    
    guess = input("Guess a letter: ")

    
    if guess in word:
        guesses.append(guess)

        if all(letter in guesses for letter in word):
            print("You win!")
            break
    else:
        lives -= 1
        if lives == 0:
            print("You lose!") 

    

# The user has lost the game.

