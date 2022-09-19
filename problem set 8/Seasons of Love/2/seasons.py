from datetime import date
import sys
import re
import inflect

def main():
    birth_date = convert_date(input("Date of Birth: "))
    today = date.today()
    minutes = convert_day_diff_to_minute(birth_date, today)
    print(translate_num_to_eng(minutes))



def convert_date(s):
    if re.search(r"\d\d\d\d-\d\d-\d\d", s):
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
    if isinstance(old_date, date) and isinstance(new_date, date):
        diff = new_date - old_date
        minutes = diff.days * 24 * 60
        return minutes
    else:
        sys.exit("Invalid date")

def translate_num_to_eng(s):
    p = inflect.engine()
    w = p.number_to_words(s, andword="")
    ww = f"{w.capitalize()} minutes"
    return ww




if __name__ == "__main__":
    main()