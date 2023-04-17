import random

# Set the range for the random number
min_number = 1
max_number = 10

# Generate a random number for the user to guess
number = random.randint(min_number, max_number)

# Set the number of guesses allowed
max_guesses = 3
num_guesses = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between", min_number, "and", max_number)

# Loop through the number of guesses allowed
while num_guesses < max_guesses:
    # Prompt the user to enter their guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number.")
        break

    # If the guess is incorrect, provide a hint
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    # Increase the number of guesses made
    num_guesses += 1

# If the user has used up all their guesses and not guessed correctly, provide the answer
if num_guesses == max_guesses:
    print("Sorry, you have used up all your guesses.")
    print("The number I was thinking of was:", number)

