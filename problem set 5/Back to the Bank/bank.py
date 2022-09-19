


def main():
    greeting = input("What do you say for greeting? ")
    print("$", value(greeting), sep = "")


def value(greeting):
    ci_greeting = greeting.lower().strip()

    if ci_greeting[0:5] == "hello":
        return 0
    elif ci_greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()