

def main():
    child = int(input("How many child tickets would you like? "))
    adult = int(input("How many adult tickets would you like? "))
    senior = int(input("How many senior tickets would you like? "))

    p_sum = (child * 5) + (adult * 10) + (senior * 8)

    print(f"Total Price: {p_sum} £")


if __name__ == "__main__":
    main()
