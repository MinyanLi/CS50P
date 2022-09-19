import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if re.fullmatch(r"<iframe.*></iframe>", s):
        if re.search(r"https?://(www.)?youtube.com/embed/([a-zA-Z0-9]*)", s):
            src = re.search(r"https?://(www.)?youtube.com/embed/([a-zA-Z0-9]*)", s)
            link = src.group(2)
            name = "https://youtu.be/" + link
            return name
        else:
            return None
    else:
        return None





if __name__ == "__main__":
    main()