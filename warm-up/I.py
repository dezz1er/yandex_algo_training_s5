n = int(input())
year = int(input())
leap_year = False
if year % 100:
    if year % 4 == 0:
        leap_year = True
else:
    if year % 400 == 0:
        leap_year = True
if not leap_year:
    buff = {
        "January": 0,
        "February": 31,
        "March": 59,
        "April": 90,
        "May": 120,
        "June": 151,
        "July": 181,
        "August": 212,
        "September": 243,
        "October": 273,
        "November": 304,
        "December": 334,
    }
else:
    buff = {
        "January": 0,
        "February": 31,
        "March": 60,
        "April": 91,
        "May": 121,
        "June": 152,
        "July": 182,
        "August": 213,
        "September": 244,
        "October": 274,
        "November": 305,
        "December": 335,
    }
day = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}
day_ = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

holiday = [0] * n
res = [0] * 7
for i in range(n):
    a = input().split()
    holiday[i] = int(a[0]) + buff[a[1]]
x = input()
if not leap_year:
    res[day[x]] += 1
else:
    res[day[x]] += 1
    res[(day[x] + 1) % 7] += 1
for h in holiday:
    res[(h - 1 + day[x]) % 7] -= 1
print(day_[res.index(max(res))], day_[res.index(min(res))])
