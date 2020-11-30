import datetime as dt
def string_to_date(string):
    year = int(string[:4])
    month = int(string[5:7])
    days = int(string[8:])
    return dt.date(year, month, days)