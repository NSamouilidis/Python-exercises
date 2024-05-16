

def main():
    n = int(input("Please enter the size (no of rows) of the triangle you wish to display:\n"))
    point = 0
    star = 1
    while n > point:
        print("*" * star)
        point += 1
        star += 1


if __name__ == "__main__":
    main()
