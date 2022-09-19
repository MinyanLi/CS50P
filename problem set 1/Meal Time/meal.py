def main():
    t = input("What time is it now? ")
    T = t.lower().strip()
    CT = convert(T)
    if 7 <= CT <= 8:
        print("breakfast time")
    if 12 <= CT <= 13:
        print("lunch time")
    if 18 <= CT <= 19:
        print("dinner time")


def convert(time):
    space_count = time.count(" ")
    if space_count == 0:
        t_twenty_four = time.split(":")
        h = int(t_twenty_four[0])
        m = int(t_twenty_four[1])
        t = h + m / 60
    if space_count == 1:
        number_txt_sep = time.split(" ")
        t_twelve = number_txt_sep[0].split(":")
        h_twelve = int(t_twelve[0])
        m_twelve = int(t_twelve[1])
        if number_txt_sep[-1] == "a.m.":
            t = h_twelve + m_twelve / 60
        if number_txt_sep[-1] == "p.m.":
            t = h_twelve + 12 + m_twelve / 60
    return t



main()