months_word = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

months_dict = dict(zip(months_word, months_number))

while True:
    try:
        x = input("Date: ").strip()
        if x[0].isdigit():
            m, d, y = x.split(sep = "/")
            d = int(d)
            m = int(m)
            if d > 31:
                d = int("not a date")
            if m > 12:
                m = int("not a date")
            for i in months_dict:
                if m == int(months_dict[i]):
                    print(y,end = "-")
                    print(f"{m:02}",end = "-")
                    print(f"{d:02}")

        else:
            if x.count(",") == 0:
                k = int("format incorrect")
                print(k)
            else:
                z = x.replace(",", "")
                m, d, y = z.split(sep = " ")
                d = int(d)
                if d > 31:
                    d = int("not a date")
                for i in months_dict:
                    if m == i:
                        print(y,end = "-")
                        m = int(months_dict[i])
                        print(f"{m:02}",end = "-")
                        print(f"{d:02}")
        break
    except ValueError:
        pass
