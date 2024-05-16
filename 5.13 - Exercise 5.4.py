

def arithmetic_sum():
    total_sum = d * (2 * s + (d - 1) * m) // 2
    return total_sum

if __name__ == "__main__":
    print(arithmetic_sum(1, 1, 100)) # prints the return value - 5050
    print(arithmetic_sum(3, 2, 15)) # prints the return value - 255
    print(arithmetic_sum(10, 4, 5)) # prints the return value - 90
    print(arithmetic_sum(-5, -2, 20)) # prints the return value - -480