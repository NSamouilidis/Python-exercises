

def main():
    Celsius = float(input("Please enter the temperature in Celsius:"))
    if Celsius >= 0:
        Fahrenheit = (9 / 5) * Celsius + 32

        print(f"{Celsius} Celsius is equivalent to {Fahrenheit} Fahrenheit.")
    else:
        print("ERROR: You must enter a value of 0 or greater.")


if __name__ == "__main__":
    main()
