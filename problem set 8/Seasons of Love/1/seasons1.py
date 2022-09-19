from datetime import date
import sys
import re
import inflect


def main():

    birth_date = input("Date of Birth: ")
    today = date.today()

    # get birthdate
    if re.search(r"\d\d\d\d-\d\d-\d\d", birth_date):
        birthdate = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", birth_date)
        birthy = birthdate.group(1)
        birthm = birthdate.group(2)
        birthd = birthdate.group(3)
        birthy = int(birthy)
        birthm = int(birthm)
        birthd = int(birthd)
        try:
            birthdate = date(birthy, birthm, birthd)
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")

    # get number of days and calculate to minutes
    age = today - birthdate
    minutes = round(age.total_seconds() / 60)

    # translate minutes from number to words
    p = inflect.engine()
    w_minutes = p.number_to_words(minutes)
    w_minutes = w_minutes.replace(" and ", " ")

    print(f"{w_minutes.capitalize()} minutes")









if __name__ == "__main__":
    main()









