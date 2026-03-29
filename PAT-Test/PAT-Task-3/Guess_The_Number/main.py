"""Guess the Number game - player guesses a random number between 1 and 10."""
import random                                       # Import the random module

number = random.randint(1, 10)                      # Generate a random number between 1 and 10
guess = 0                                           # Set the variable to 0 to start the game

print("Guess the number between 1 and 10!")

while guess != number:
    guess = int(input("Type your guess: [1-10] "))  # Get input from the player
    
    if guess < number:                              # Check if the player's guess is too low, too high, or correct
        print("Your guess is too low!")
    elif guess > number:
        print("Your guess is too high!")
    else:
        print("You guess is correct!")              # If the guess is correct, print a congratulatory message