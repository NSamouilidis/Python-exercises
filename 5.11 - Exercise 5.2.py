def convert_temp(temp, fahrenheit=False):
    zerocelsius = -273.15
    zerofahrenheit = -459.67

    if not fahrenheit:
        if temp < zerocelsius:
            return None
        else:
            result = (9/5) * temp + 32
    else:
        if temp < zerofahrenheit:
            return None
        else:
            result = (5/9) * (temp - 32)

    return round(result, 2)


if __name__ == "__main__":
    # I would comment some of these out as you build up parts of convert_temp
    # e.g. just start by getting convert_temp(20) to work
    print(convert_temp(20)) # Prints 68.0
    #print(convert_temp(-10)) # Prints 14.0

    #print(convert_temp(68, fahrenheit=True)) # Prints 20.0
    #print(convert_temp(-100, fahrenheit=True)) # Prints -73.33
