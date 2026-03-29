"""Word Scramble game - player unscrambles a randomly selected word."""
import random                                            # Import the random module

words = ['apple', 'orange', 'mango']                     # List of words for the player to guess

word = random.choice(words)                              # Select a random word from the list

scrambled = ''.join(random.sample(word, len(word)))      # Create a scrambled version 

print("\nUnscramble this word: " + scrambled)            # Ask the player to unscramble the word

while True:
    guess = input("Your guess: ")
    if guess == word:                                    # If correct, congratulate and break
        print("Correct!")
        break
    else:
        print("Wrong! Try again.")                       # Offer another attempt regardless of count

