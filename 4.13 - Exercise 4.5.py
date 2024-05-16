# The Number Guessing Game
import random


def main():
    secret_guess = random.randint(1,10)
    print("Welcome to the Number Guessing Game!")
    print("You need to try and guess the number between 1 and 10...")
    print("If you wish to exit the game enter 0...")
    guesses = 1
    guess = int(input("Please enter a guess:\n"))

    while guess != secret_guess:
        if guess != 0:
            guesses += 1
            guess = int(input("Please enter a guess:\n"))
            if guess > secret_guess:
                print("Your guess is too high, please try again.")
            elif guess < secret_guess:
                print("Your guess is too low, please try again.")
            elif guess == 0:
                print(f"Program exited. The correct answer was {secret_guess}")
            else:
                print(f"Well done the correct answer was {secret_guess}")
                print(f"You took {guesses} guesses")
        else:
            print("Program exited")
            break


if __name__ == "__main__":
    main()
