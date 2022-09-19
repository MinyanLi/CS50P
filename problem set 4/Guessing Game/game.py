def main():
    import random
    import sys

    level = input_positive_integer("Level: ")
    n = random.randint(1, level)

    while True:
        guess = input_positive_integer("Guess: ")
        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            sys.exit("Just right!")





def input_positive_integer(text):
    while True:
        try:
            n = int(input(text))
            if n <= 0:
                continue
            break
        except ValueError:
            pass
    return n


main()









