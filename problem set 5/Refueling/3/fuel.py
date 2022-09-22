def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass



def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    f = x / y
    if f > 1:
        raise ValueError
    return round(f * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
