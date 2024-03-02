def leap_year(year):
    if (year % 4==0 and year % 100 !=0) or (year % 400 ==0):
        return "leap year"
    else:
        return "Not a leap year"
year=int(input("enter the year which you want to check:"))
if leap_year(year)=="leap year":
    print(f"{year} is a leap year ")
else:
    print(f"{year} is not a leap year")
