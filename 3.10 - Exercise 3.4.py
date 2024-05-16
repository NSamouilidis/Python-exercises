

def main():
    copies = float(input("Please enter the number of copies of the software you wish to purchase:"))

    total = copies * 99
    cost = total

    if copies == 5 or copies <= 9:
        discount = total * 0.1
        print("You have been given a 10% discount on the normal price of £99.")
        print(f"The total cost is {cost - discount:.2f}")
    elif copies == 10 or copies <= 19:
        discount = total * 0.2
        print("You have been given a 20% discount on the normal price of £99.")
        print(f"The total cost is {cost + discount:.2f}")
    elif copies == 20 or copies <= 49:
        discount = total * 0.3
        print("You have been given a 30% discount on the normal price of £99.")
        print(f"The total cost is {cost - discount:.2f}")
    elif copies == 50 or copies <= 99:
        discount = total * 0.4
        print("You have been given a 40% discount on the normal price of £99.")
        print(f"The total cost is {cost - discount:.2f}")
    else:
        discount = total * 0.5
        print("You have been given a 50% discount on the normal price of £99.")
        print(f"The total cost is {cost - discount:.2f}")


if __name__ == "__main__":
    main()
