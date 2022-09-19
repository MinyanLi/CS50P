def main():
    while True:
        date = input("Date: ").strip()
        if date_number_format(date) != False:
            a = date_number_format(date)
            print(a[0], f"{a[1]:02}", f"{a[2]:02}", sep = "-", end = "")
            break
        elif date_word_format(date) != False:
            b = date_word_format(date)
            print(b[0], f"{b[1]:02}", f"{b[2]:02}", sep = "-", end = "")
            break
        else:
            pass





def date_number_format(prompt):

    # correct format should be m/d/yyyy or mm/d/yyyy or m/dd/yyyy or mm/dd/yyyy

    # make sure all are numbers
    number_and_sep = "0123456789" + "/"
    c = []
    for i in prompt:
        if number_and_sep.count(i) == 0:
            c.append(False)
        else:
            c.append(True)
    y = all(c)
    if y == False:
        return False


    # 8-10 characters
    if len(prompt) < 8 or len(prompt) > 10:
        return False

    # contain 2 seperators
    if prompt.count("/") != 2:
        return False

    # maker sure last seperator correct position
    if prompt[-5] != "/":
        return False

    # numbers are within range
    m, d, y = prompt.split("/")
    mm = int(m)
    dd = int(d)
    yyyy = int(y)

    if mm > 12 or dd > 31:
        return False

    # not start with 0
    if m[0] == "0" or d[0] == "0":
        return False


    # conclude checklist
    return yyyy, mm, dd






def date_word_format(prompt):

    # correct format should be eg. "January d, yyyy"
    months = [
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

    p_space_sep = prompt.split(" ")
    m = p_space_sep[0]

    # first substring is month full name with capitalization
    if months.count(m) != 1:
        return False


    # except for month, all are numbers and sperators
    p_minus_m = prompt.replace(m, "")
    number_and_sep = "0123456789" + " " + ","
    c = []
    for i in p_minus_m:
        if number_and_sep.count(i) == 0:
            c.append(False)
        else:
            c.append(True)
    y = all(c)
    if y == False:
        return False


    # other than month, 8 - 9 characters in total (including 2 space and 1 comma)
    if len(p_minus_m) < 8 or len(p_minus_m) > 9:
        return False


    # before year is ", "
    if prompt[-5] != " " or prompt[-6] != ",":
        return False


    # only 2 space
    if prompt.count(" ") != 2:
        return False


    # not start with 0
    if prompt[-8] == "0":
        return False

    # switch to number
    prompt = prompt.replace(",", "")
    m, d, y = prompt.split(" ")
    mm = int(months.index(m) + 1)
    dd = int(d)
    yyyy = int(y)

    # numbers are within range
    if dd > 31:
        return False

    # conclude checklist
    return yyyy, mm, dd








main()

