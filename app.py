import datetime as dt
import os
from resources import moon

from flask import Flask
app = Flask(__name__)


@app.route('/phase')
@app.route('/phase/<int:year>/<int:month>/<int:day>')
def phase(year=None, month=None, day=None):
    if year is None and month is None and day is None:
        today = dt.datetime.now()
        today -= dt.timedelta(days=1) # 2020 leap day correction
        year, month, day = today.year, today.month, today.day
    p = (moon.julian(year, month, day) - moon.julian(2000, 1, 6)) % 29.530588853

    if p < 1.84566:
        return "🌑"  # new
    elif p < 5.53699:
        return "🌒"  # waxing crescent
    elif p < 9.22831:
        return "🌓"  # first quarter
    elif p < 12.91963:
        return "🌔"  # waxing gibbous
    elif p < 16.61096:
        return "🌕"  # full
    elif p < 20.30228:
        return "🌖"  # waning gibbous
    elif p < 23.99361:
        return "🌗"  # last quarter
    elif p < 27.68493:
        return "🌘"  # waning crescent
    else:
        return "🌑"  # new
