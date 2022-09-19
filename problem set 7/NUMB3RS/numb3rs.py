import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(r"(\d+\.){3}(\d+)", ip):
        a, b, c, d = ip.split(".")
        A = int(a)
        B = int(b)
        C = int(c)
        D = int(d)
        if 0 <= A <= 255 and 0 <= B <= 255 and 0 <= C <= 255 and 0 <= D <= 255:
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
