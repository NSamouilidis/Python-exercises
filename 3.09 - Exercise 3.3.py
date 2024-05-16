

def main():
    conv = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:"))
    if conv == 1:
        celsius = float(input("Please enter the temperature in Celsius:"))
        if celsius >= 0:
            Fahrenheit = (9 / 5) * celsius + 32

            print(f"{celsius} Celsius is equivalent to {Fahrenheit} Fahrenheit.")
    elif conv == 2:

        Fahrenheit = float(input("Please enter the temperature in Fahrenheit:"))
        if Fahrenheit >= 0:
            Celsius = (5 / 9) * (Fahrenheit - 32)
            print(f"{Fahrenheit}Fahrenheit is equivalent to {Celsius} Celsius.")
    else:
        print("ERROR: Invalid option")


if __name__ == "__main__":
    main()
