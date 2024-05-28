import re

date_regex = re.compile(r"""
    (?P<day>0[1-9]|[12][0-9]|3[01])  
    /                                
    (?P<month>0[1-9]|1[0-2])         
    /                                
    (?P<year>[12][0-9]{3})           
    """, re.VERBOSE)

def is_valid_date(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        days_in_month[1] = 29  

    return 1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]

text = "今日は24/05/2024で、明日は25/13/2024です。過去の日付としては31/04/2023があります。"

matches = date_regex.finditer(text)
for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')

    if is_valid_date(day, month, year):
        print(f"{day}/{month}/{year}")
    else:
        print(f"{day}/{month}/{year}")
