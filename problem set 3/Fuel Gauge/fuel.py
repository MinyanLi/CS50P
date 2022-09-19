
while True:
    try:
        fractions = input("fraction: ")
        X, Y = fractions.split(sep = "/")
        X = int(X)
        Y = int(Y)
        if X > Y:
            X = int("big")
        if Y == 0:
            Y = int("zero")
        break

    except ValueError:
        pass

percent = round (X / Y * 100)

if percent <= 1:
    print("E")
if percent >= 99:
    print("F")
if 1 < percent < 99:
    print(percent,"%", sep = "")