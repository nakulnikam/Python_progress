def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example usage:
year = int(input("Enter a year: "))
print(is_leap_year(year))