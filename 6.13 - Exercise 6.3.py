

def main():
    numbers = []

    for _ in range(10):
        user_input = input("Please enter the next number: ")

        if user_input.lower() == 'q':
            break

        numbers.append(int(user_input))

    if not numbers:
        print("No numbers entered.")
    else:
        print("The reverse of the numbers entered is:")
        for num in reversed(numbers):
            print(num)


if __name__ == "__main__":
    main()  # call the main function
