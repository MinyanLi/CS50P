import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = len(re.findall(r"\bum\b", s.lower()))
    return count



if __name__ == "__main__":
    main()