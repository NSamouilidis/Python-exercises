

def main():
    Celsius = float(input("Please enter the temperature in Celsius:  "))

    Fahrenheit = round((9 / 5) * Celsius + int(32), 2)

    print(f" {Celsius} Celsius is equivalent to {Fahrenheit} Fahrenheit.")


if __name__ == "__main__":
    main()
