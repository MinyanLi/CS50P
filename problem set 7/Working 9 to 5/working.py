import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = []
    if re.search(r"(\d?\d:\d\d AM)|((^| )\d?\d AM)|(\d?\d:\d\d PM)|((^| )\d?\d PM)", s):
        if re.search(r"(.+) to (.+)", s):
            Hours = re.search(r"(.+) to (.+)", s)
            begin = Hours.group(1)
            end = Hours.group(2)

            if re.search(r"\d?\d:\d\d AM", begin):
                am1 = re.search(r"(\d?\d):(\d\d) AM", begin)
                am1_h = am1.group(1)
                am1_h = int(am1_h)
                am1_m = am1.group(2)
                am1_m = int(am1_m)
                if am1_h == 12:
                    am1_h = 0
                if am1_h > 12 or am1_m >= 60:
                    raise ValueError()
                else:
                    t = f"{am1_h:02}" + ":" + f"{am1_m:02}"
                    time.append(t)

            if re.search(r"((^| )\d?\d AM)", begin):
                am2 = re.search(r"(\d?\d) AM", begin)
                am2_h = am2.group(1)
                am2_h = int(am2_h)
                if am2_h == 12:
                    am2_h = 0
                if am2_h > 12:
                    raise ValueError()
                else:
                    t = f"{am2_h:02}" + ":" + "00"
                    time.append(t)

            if re.search(r"\d?\d:\d\d PM", begin):
                pm1 = re.search(r"(\d?\d):(\d\d) PM", begin)
                pm1_h = pm1.group(1)
                pm1_h = int(pm1_h)
                if pm1_h != 12:
                    pm1_h = pm1_h + 12
                pm1_m = pm1.group(2)
                pm1_m = int(pm1_m)
                if pm1_h > 24 or pm1_m >= 60:
                    raise ValueError()
                else:
                    t = f"{pm1_h:02}" + ":" + f"{pm1_m:02}"
                    time.append(t)

            if re.search(r"((^| )\d?\d PM)", begin):
                pm2 = re.search(r"(\d?\d) PM", begin)
                pm2_h = pm2.group(1)
                pm2_h = int(pm2_h)
                if pm2_h != 12:
                    pm2_h = pm2_h + 12
                if pm2_h > 24:
                    raise ValueError()
                else:
                    t = f"{pm2_h:02}" + ":" + "00"
                    time.append(t)


            if re.search(r"\d?\d:\d\d AM", end):
                am1e = re.search(r"(\d?\d):(\d\d) AM", end)
                am1e_h = am1e.group(1)
                am1e_h = int(am1e_h)
                am1e_m = am1e.group(2)
                am1e_m = int(am1e_m)
                if am1e_h == 12:
                    am1e_h = 0
                if am1e_h > 12 or am1e_m >= 60:
                    raise ValueError()
                else:
                    t = f"{am1e_h:02}" + ":" + f"{am1e_m:02}"
                    time.append(t)

            if re.search(r"((^| )\d?\d AM)", end):
                am2e = re.search(r"(\d?\d) AM", end)
                am2e_h = am2e.group(1)
                am2e_h = int(am2e_h)
                if am2e_h == 12:
                    am2e_h = 0
                if am2e_h > 12:
                    raise ValueError()
                else:
                    t = f"{am2e_h:02}" + ":" + "00"
                    time.append(t)

            if re.search(r"\d?\d:\d\d PM", end):
                pm1e = re.search(r"(\d?\d):(\d\d) PM", end)
                pm1e_h = pm1e.group(1)
                pm1e_h = int(pm1e_h)
                if pm1e_h != 12:
                    pm1e_h = pm1e_h + 12
                pm1e_m = pm1e.group(2)
                pm1e_m = int(pm1e_m)
                if pm1e_h > 24 or pm1e_m >= 60:
                    raise ValueError()
                else:
                    t = f"{pm1e_h:02}" + ":" + f"{pm1e_m:02}"
                    time.append(t)

            if re.search(r"((^| )\d?\d PM)", end):
                pm2e = re.search(r"(\d?\d) PM", end)
                pm2e_h = pm2e.group(1)
                pm2e_h = int(pm2e_h)
                if pm2e_h != 12:
                    pm2e_h = pm2e_h + 12
                if pm2e_h > 24:
                    raise ValueError()
                else:
                    t = f"{pm2e_h:02}" + ":" + "00"
                    time.append(t)

        else:
            raise ValueError()
    else:
        raise ValueError()


    if len(time) != 2:
        raise ValueError()
    else:
        return f"{time[0]} to {time[1]}"







if __name__ == "__main__":
    main()