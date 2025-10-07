def is_leap_year(year):
    return (year%400==0) or (year%4==0 and year%100 !=0)
month_days= {
    "January":31, "February":28, "March":31, "April":30, "May":31,
    "June":30, "July":31, "August":31, "September":30,
    "October":31, "November":30, "December":31
}
month=input("Enter the name of a month: ")
if month=="February":
    year=int(input("Enter a year: "))
    days = 29 if is_leap_year(year) else 28
    print(f"{month} has {days} days.")
else:
    print(f"{month} has {month_days[month]} days.")