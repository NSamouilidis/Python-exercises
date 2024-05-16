

def main():
    print("This program calculates the largest number from a series of numbers entered.")
    bigger = 0
    while True:
        number = int(input("Please enter a number. Enter 0 to stop\n"))
        if number > bigger:
            bigger = number
        elif bigger == 0:
            print("No numbers entered.")
        elif number == 0:
            print(f"The largest of the numbers entered is {bigger}")
            break


if __name__ == "__main__":
    main()
