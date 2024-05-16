

def main():
    print("This program calculates the average of a series of numbers")
    numbers = []
    total = 0
    while True:
        user_input = float(input("Please enter a number. Enter 0 to stop "))
        if user_input == 0:
            break
        numbers.append(user_input)
        total += user_input
    if user_input == 0 and len(numbers) < 1:
        print("No numbers entered.")
    else:
        print(f"The average of the numbers entered is {total / len(numbers)}")


if __name__ == "__main__":
    main()
