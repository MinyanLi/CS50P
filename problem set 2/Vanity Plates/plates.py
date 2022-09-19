def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    an = alpha + num
    checking_list = []


    # all are letters and numbers
    c = []
    for i in s:
        if an.count(i) == 0:
            c.append(False)
        else:
            c.append(True)
    y = all(c)
    if y == True:
        checking_list.append(True)
    else:
        checking_list.append(False)


    # 2-6 characters
    if 2 <= len(s) <= 6:
        checking_list.append(True)
    else:
        checking_list.append(False)

    # first 2 characters are letters
    if len(s) >= 2:
        if alpha.count(s[0]) == 0 or alpha.count(s[1]) == 0:
            checking_list.append(False)
        else:
            checking_list.append(True)

    # numbers are at the end
    check = ""
    for i in s:
        if alpha.count(i) != 0:
            check = check + "1"
        if num.count(i) != 0:
            check = check + "0"
    if check.count("01") != 0:
        checking_list.append(False)
    else:
        checking_list.append(True)

    # the first number no 0
    for i in s:
        if num.count(i) == 0:
            checking_list.append(True)
        else:
            snum = ""
            for i in s:
                if num.count(i) != 0:
                    snum = snum + i
            if snum[0] == "0":
                 checking_list.append(False)
            else:
                checking_list.append(True)

# conclude checklist
    x = all(checking_list)
    if x == True:
        return True
    else:
        return False



main()