

def num_digits(x):
    if not isinstance(x, int) or x <= 0:
        return print("Invalid input.")

    digits = 0
    while x >= 1:
        x /= 10
        digits += 1

    return digits
def main():
    try:
        number = int(input("Please enter a positive whole number:\n"))
        digits = num_digits(number)

        if digits is not None:
            print(f"{number} has {digits} {'digit' if digits == 1 else 'digits'}.")
        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")
# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":

    main()
