def main():

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

    while True:
        date = input("Date: ").strip()
        if date_number_format(date) == True:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            print(y, end = "-")
            print(f"{m:02}", end = "-")
            print(f"{d:02}", end = "")
            break
        elif date_word_format(date) == True:
            date = date.replace(",", "")
            m, d, y = date.split(" ")
            mn = months.index(m) + 1
            d = int(d)
            print(y, end = "-")
            print(f"{mn:02}", end = "-")
            print(f"{d:02}", end="")
            break
        else:
            pass





def date_number_format(prompt):

    # correct format should be m/d/yyyy or mm/d/yyyy or m/dd/yyyy or mm/dd/yyyy

    checking_list = []

    # make sure all are numbers
    number_and_sep = "0123456789" + "/"
    c = []
    for i in prompt:
        if number_and_sep.count(i) == 0:
            c.append(False)
        else:
            c.append(True)
    y = all(c)
    if y == True:
        checking_list.append(True)
    else:
        return False


    # 8-10 characters
    if 8 <= len(prompt) <= 10:
        checking_list.append(True)
    else:
        return False

    # contain 2 seperators
    if prompt.count("/") == 2:
        checking_list.append(True)
    else:
        return False

    # maker sure last seperator correct position
    if len(prompt) > 5:
        if prompt[-5] == "/":
            checking_list.append(True)
        else:
            return False
    else:
        return False

    # numbers are within range
    m, d, y = prompt.split("/")
    m = int(m)
    d = int(d)
    if 0 < m < 13 and 0 < d < 32:
        checking_list.append(True)
    else:
        return False

    # not start with 0
    m, d, y = prompt.split("/")
    if m[0] == "0" or d[0] == "0":
        return False
    else:
        checking_list.append(True)


    # conclude checklist
    x = all(checking_list)
    if x == True:
        return True
    else:
        return False





def date_word_format(prompt):

    # correct format should be eg. "January d, yyyy"

    checking_list = []

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
    if months.count(m) == 1:
        checking_list.append(True)
    else:
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
    if y == True:
        checking_list.append(True)
    else:
        return False


    # other than month, 8 - 9 characters in total (including 2 space and 1 comma)
    if 8 <= len(p_minus_m) <= 9:
        checking_list.append(True)
    else:
        return False


    # before year is ", "
    if prompt[-5] == " " and prompt[-6] == ",":
        checking_list.append(True)
    else:
        return False


    # only 2 space
    if prompt.count(" ") == 2:
        checking_list.append(True)
    else:
        return False

    # numbers are within range
    prompt_no_comma = prompt.replace(",", " ")
    s = prompt_no_comma.split(" ")
    d = int(s[1])
    if 0 < d < 32:
        checking_list.append(True)
    else:
        return False


    # not start with 0
    if prompt[-8] == "0":
        return False
    else:
        checking_list.append(True)


    # conclude checklist
    x = all(checking_list)
    if x == True:
        return True
    else:
        return False


main()

