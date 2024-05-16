

def main():
    speed = (input("please give me your speed: "))
    hours = (input("How many hours has it travelled? "))

    if speed.isdigit() and hours.isdigit():
        print(f" Hours    |      Distance")
        print("---------------------------")
        h = int(hours)
        s = int(speed)
        for hour in range(h):
            print(f"{hour + 1}         |    {s * (hour + 1)}")
    else:
        print("You gave a character ")


if __name__ == "__main__":
    main()
