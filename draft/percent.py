def capital(year, add_month, percent):
    month = percent / 12
    year = year * 12
    for _ in range(1, year + 1):
        add_month = ((add_month * (month + 100)) / 100) + add_month
    return add_month 

print(capital(10, 25000, 13))