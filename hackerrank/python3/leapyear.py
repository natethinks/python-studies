def is_leap(year):
    leap = False
    if year % 4 != 0:
        return leap
    if (year % 100 == 0) & (year % 400 != 0):
        return leap
    else:
        leap = True
        return leap
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
