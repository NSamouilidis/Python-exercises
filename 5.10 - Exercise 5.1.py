

def calc_retail_price(wholesale, markup):
    retail_price = wholesale + (wholesale * markup / 100)
    return retail_price


def main():
    wholesale = int(input("Please enter a wholesale cost:"))
    markup = int(input("Please enter a markup percentage:"))
    print(f"The retail price is {calc_retail_price(wholesale, markup):.2f}")

if __name__ == "__main__":
    main() # calls the main function


