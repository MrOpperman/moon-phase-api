def julian(year, month, day):
    a = (14 - month) / 12.0
    y = year + 4800 - a
    m = (12 * a) - 3 + month
    return (
        day + (153 * m + 2) / 5.0 + (365 * y) + y / 4.0 - y / 100.0 + y / 400.0 - 32045
    )
