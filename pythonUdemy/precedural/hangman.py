import random
from  logo import hangman

# Word list
word_list = ['aardvark', 'baboon', 'camel']

# Hangman stages representing the hangman figure at each step
stages = [
    '''
         +---+
         |   |
         0   |
        /|\  |
         |   |
        / \  |
        ========== ''', '''
         +---+
         |   |
         0   |
        /|\  |
         |   |
        /    |
        ========== ''', '''
         +---+
         |   |
         0   |
        /|\  |
         |   |
             |
        ========== ''', '''
         +---+
         |   |
         0   |
        /|\  |
             |
             |
        ========== ''', '''
         +---+
         |   |
         0   |
        /|   |
             |
             |
        ========== ''', '''
         +---+
         |   |
         0   |
        /    |
             |
             |
        ========== ''', '''
         +---+
         |   |
         0   |
             |
             |
             |
        ========== ''', '''
         +---+
         |   |
             |
             |
             |
             |
        ========== ''', '''
         +---+
             |
             |
             |
             |
             |
        ========== '''
]

# Randomly choose a word
word_random = random.choice(word_list).lower()

# Initialize guessed word display and variables
guess = ['-' for _ in word_random]
wrong_guess = 0
guessed_letters = set()
max_guess = len(stages) - 1

print(hangman())
# Game loop
while wrong_guess < max_guess:
    # Display current stage of the hangman
    print(stages[-(wrong_guess+1)])
    
    # Ask the player to guess a letter
    guess_letter = input(f"Guess a letter ({''.join(guess)}): {word_random} \n").lower()
    # Validate input to allow only single alphabetic characters
    if not guess_letter.isalpha() or len(guess_letter) != 1:
        print("Please enter a single valid letter.")
        continue
    
    # Skip if letter already guessed
    if guess_letter in guessed_letters:
        print(f"You already guessed '{guess_letter}'. Try again.")
        continue
    
    # Add guessed letter to set
    guessed_letters.add(guess_letter)
    
    # Check if the guessed letter is in the word
    if guess_letter in word_random:
        for i, letter in enumerate(word_random):
            if letter == guess_letter:
                guess[i] = guess_letter
    else:
        print(f"Wrong choice! '{guess_letter}' is not in the word.")
        wrong_guess += 1  # Increase wrong guess count
        print(f"Lives remaining: {max_guess - wrong_guess}/{max_guess}")

    
    # Display the current state of the word
    final_word = ''.join(guess)
    print(f"Current word: {final_word}")
    
    # Check if the player has guessed the word
    if '-' not in guess:
        print(hangman())
        print(f"Congratulations! You've guessed the word: {final_word}")
        break

# If the player runs out of attempts, display the final stage and the correct word
if '-' in guess:
    print(hangman())
    print(f"Game over and thse hangman has zero lives left! The correct word was: {word_random}")
    print(stages[-(wrong_guess+1)])  # Show the final hangman stage
