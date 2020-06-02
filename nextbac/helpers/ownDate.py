# Script that gets the current month and year
from datetime import date


def currentDate():
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%B")
    return (month, year)
