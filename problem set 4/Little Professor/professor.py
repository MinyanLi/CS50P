import random


def main():
    level = get_level()
    correct = 0
    for i in range(1,11):
        formula = generate_integer(level)
        x = formula[0]
        y = formula[1]
        for j in range(1,4):
            answer = int(input())
            if answer != x + y:
                print("EEE")
            else:
                correct = correct + 1
                break
            if j == 3:
                print(x, " + ", y, " = ", (x + y),sep = "")
    print(correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass




def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    if level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    if level == 3:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    print(X, Y, sep = " + ", end = " = ")
    return X, Y

if __name__ == "__main__":
    main()