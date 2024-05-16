import random


def get_user_guess():
    """ gets the user input"""
    while True:
        user_input = input("Enter a number between 1 and 10 or 'q' to quit: ")
        if user_input.lower() == 'q':
            return 'q'
        elif user_input.isdigit() and 1 <= int(user_input) <= 10:
            return user_input
        else:
            print("Invalid input: Please enter a whole number between 1 and 10 or 'q' to quit")


def print_feedback(no_guesses, max_guesses, secret_num):
    """ prints the end feedback """
    if no_guesses > max_guesses:
        print("Sorry, better luck next time.")
    else:
        print(f"Well done, you used {no_guesses}/{max_guesses} guesses to guess the secret number {secret_num}.")


def main():
    secret_num = random.randint(1, 10)
    keep_going = True
    max_guesses = 3
    no_guesses = 0

    while keep_going:
        if no_guesses < max_guesses:
            guess = get_user_guess()

            if guess == "q":
                keep_going = False
            else:
                if int(guess) == secret_num:
                    keep_going = False
                else:
                    print("Incorrect, please try again\n")
        else:
            keep_going = False

        no_guesses += 1

    if guess == "q":
        print("User exited the program.")
    else:
        print_feedback(no_guesses, max_guesses, secret_num)


if __name__ == "__main__":
    main()

