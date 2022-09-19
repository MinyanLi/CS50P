def main():
    n = input("What do you want to make for emoji? ")
    m = convert(n)
    print(m)


def convert(n):
    m = n.replace(":)", "🙂").replace(":(", "🙁")
    return m

main()
