

def main():
    while True:
        fraction = input("fraction: ")
        percentage = convert(fraction)
        if percentage == False:
            pass
        else:
            break
    print(gauge(percentage)[0], gauge(percentage)[1], sep ="")


def convert(fraction:str):
    try:
        while True:
            X, Y = fraction.split(sep = "/")
            X = int(X)
            Y = int(Y)
            if X > Y:
                return False
            elif Y == 0:
                return False
            else:
                percent = round (X / Y * 100)
                return percent
    except ValueError:
        return False


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    if 1 < percentage < 99:
        return percentage, "%"


if __name__ == "__main__":
    main()
