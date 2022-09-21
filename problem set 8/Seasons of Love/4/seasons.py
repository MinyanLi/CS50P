from datetime import date
import sys
import re
import inflect
p = inflect.engine()

class Seasons:
    def __init__(self, birthdate, word_minutes):
        self.birthdate = birthdate
        self.word_minutes = word_minutes
    def __str__(self):
        return f"{self.word_minutes.capitalize()} minutes"

def get_date(s):
    if re.fullmatch(r"\d\d\d\d-\d\d-\d\d", s):
        ss = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", s)
        y = ss.group(1)
        m = ss.group(2)
        d = ss.group(3)
        y = int(y)
        m = int(m)
        d = int(d)
        try:
            bd = date(y, m, d)
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")
    return bd


def convert_day_diff_to_minute(old_date, new_date):
    diff = new_date - old_date
    minutes = diff.days * 24 * 60
    return minutes



def main():
    s = input("Date of Birth: ")
    birthdate = get_date(s)
    today = date.today()
    minutes = convert_day_diff_to_minute(birthdate, today)
    word_minutes = p.number_to_words(minutes, andword="")
    print(Seasons(birthdate, word_minutes))


if __name__ == "__main__":
    main()