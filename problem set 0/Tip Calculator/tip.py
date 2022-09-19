def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    symble, money = d.split("$")
    money_float = float(money)
    return money_float


def percent_to_float(p):
    percent_number, percent_symble = p.split("%")
    percent_float = float(percent_number) / 100
    return percent_float


main()