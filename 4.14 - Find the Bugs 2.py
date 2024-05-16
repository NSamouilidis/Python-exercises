

def main():
    # Fix the program so that it correctly prints out as the example and passes the tests. There are a number of bugs!

    # Do not touch this line
    input_list = list(input("Please enter a list of strings separated by a comma.\n"
                            "e.g. one,two,three,four,five\n\n").split(','))

    min_index = 0
    max_index = 0
    sum = 0

    i =0

    while i < len(input_list):
        sum += len(input_list[i])

        if len(input_list[i]) > len(input_list[max_index]):
            max_index = i

        if len(input_list[i]) < len(input_list[min_index]):
            min_index = i

        i += 1

    print(f"The minimum length of a string is {len(input_list[min_index])}")
    print(f"The maximum length of a string is {len(input_list[max_index])}")
    print(f"The average length of the strings in the list is{sum / len(input_list): .2f}")


if __name__ == "__main__":
    main()
