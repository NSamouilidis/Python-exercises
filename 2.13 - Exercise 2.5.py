import math

def main():
    length = float(input("Please enter the length of the wall:"))
    height = float(input("Please enter the height of the wall:"))

    sum_lh = int(length * height)
    con = math.ceil((sum_lh / 20))
    print(f"You require {con} cans of paint.")


if __name__ == "__main__":
    main()
