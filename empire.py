import datetime
import suntime
import pymeeus
from pymeeus.Sun import Sun

places = [
    {"territory": "Britain", "name": "London", "lat": 51.507222, "lon": -0.1275},
    {"territory": "Akrotiri and Dhekelia", "name": "Akrotiri", "lat": 34.590278, "lon": 32.987778},
    {"territory": "Akrotiri and Dhekelia", "name": "Dhekelia", "lat": 35.0174, "lon": 33.7734},
    {"territory": "Anguilla", "name": "Sombrero", "lat": 8.589167, "lon": -63.425278},
    {"territory": "Anguilla", "name": "Dog Island", "lat": 18.278333, "lon": -63.253333},
    {"territory": "Anguilla", "name": "Scrub Island", "lat": 18.2875, "lon": -62.947222},
    {"territory": "Anguilla", "name": "Anguillita", "lat": 18.158139, "lon": -63.175722},
    {"territory": "Bermuda", "name": "Sandys Parish", "lat": 32.3, "lon": -64.866667},
    {"territory": "Bermuda", "name": "St George's Parish", "lat": 32.371667, "lon": -64.675556},
    {"territory": "British Antarctic Territory", "name": "South Pole", "lat": -90, "lon": 0},
    {"territory": "British Antarctic Territory", "name": "Halley Research Station", "lat": -75.568056, "lon": -25.508333},
    {"territory": "British Antarctic Territory", "name": "Rothera Research Station", "lat": -67.568783, "lon": -68.125028},
    {"territory": "British Virgin Islands", "name": "Anegada", "lat": 18.733333, "lon": -64.333333},
    {"territory": "British Virgin Islands", "name": "Jost Van Dyke", "lat": 18.45, "lon": -64.75},
    {"territory": "Cayman Islands", "name": "George Town", "lat": 18.45, "lon": -64.75},
    {"territory": "Cayman Islands", "name": "Cayman Brac", "lat": 19.296389, "lon": -81.381667},
    {"territory": "Falkland Islands", "name": "Stanley", "lat": -51.695, "lon": -57.850556},
    {"territory": "Gibraltar", "name": "The Rock", "lat": 36.124472, "lon": -5.343111},
    {"territory": "Montserrat", "name": "Brades", "lat": 16.792778, "lon": -62.210556},
    {"territory": "Pitcairn Islands", "name": "Oeno Island", "lat": -23.926667, "lon": -130.737222},
    {"territory": "Pitcairn Islands", "name": "Ducie Island", "lat": -24.674444, "lon": -124.786111},
    {"territory": "Saint Helena, Ascension and Tristan da Cunha", "name": "Jamestown", "lat": -15.924444, "lon": -5.718056},
    {"territory": "Saint Helena, Ascension and Tristan da Cunha", "name": "Georgetown", "lat": -7.928611, "lon": -14.411667},
    {"territory": "Saint Helena, Ascension and Tristan da Cunha", "name": "Gough Island", "lat": -40.32, "lon": -9.94},
    {"territory": "Saint Helena, Ascension and Tristan da Cunha", "name": "Edinburgh of the Seven Seas", "lat": -37.066667, "lon": -12.316667},
    {"territory": "Saint Helena, Ascension and Tristan da Cunha", "name": "Inaccessible Island", "lat": -37.3, "lon": -12.68},
    {"territory": "South Georgia and the South Sandwich Islands", "name": "South Georgia", "lat": -54.4, "lon": -36.7},
    {"territory": "South Georgia and the South Sandwich Islands", "name": "Thule Island", "lat": -59.44, "lon": -27.38},
    {"territory": "South Georgia and the South Sandwich Islands", "name": "Montague Island", "lat": -58.45, "lon": -26.36},
    {"territory": "South Georgia and the South Sandwich Islands", "name": "Zavodovski Island", "lat": -56.3, "lon": -27.58},
    {"territory": "Turks and Caicos Islands", "name": "West Caicos", "lat": 21.666667, "lon": -72.458333},
    {"territory": "Turks and Caicos Islands", "name": "Cockburn Town", "lat": 21.459, "lon": -71.139},

    {"territory": "British Indian Ocean Territory", "name": "Egmont Islands", "lat": -6.666667, "lon": 71.35},
    {"territory": "British Indian Ocean Territory", "name": "Diego Garcia", "lat": -7.313333, "lon": 72.411111},
]

start = datetime.datetime.fromisoformat('2026-01-01T00:00:00Z')
end = start + datetime.timedelta(days=366)
one_day = datetime.timedelta(days=1)

spring_equinox_components = Sun.get_equinox_solstice(2026, target="spring").get_full_date(utc=True)
spring_equinox = datetime.datetime(spring_equinox_components[0], spring_equinox_components[1], spring_equinox_components[2], spring_equinox_components[3], spring_equinox_components[4], int(spring_equinox_components[5]), tzinfo=datetime.timezone.utc)

autumn_equinox_components = Sun.get_equinox_solstice(2026, target="autumn").get_full_date(utc=True)
autumn_equinox = datetime.datetime(autumn_equinox_components[0], autumn_equinox_components[1], autumn_equinox_components[2], autumn_equinox_components[3], autumn_equinox_components[4], int(autumn_equinox_components[5]), tzinfo=datetime.timezone.utc)

def sun_is_up(date, place):
    if date > spring_equinox and date < autumn_equinox:
        return place["lat"] > 0
    else:
        return place["lat"] < 0
    
date = start
while date < end:
    times = []
    day = {}
    for place in places:
        sun = suntime.Sun(place["lat"], place["lon"])
        try:
            sunrise = sun.get_sunrise_time(date)
            times.append({"name": place["name"], "type": "sunrise", "time": sunrise})
        except suntime.SunTimeException as e:
            if sun_is_up(date, place):
                day[place["name"]] = date
            continue
        try:
            sunset = sun.get_sunset_time(date)
            times.append({"name": place["name"], "type": "sunset", "time": sunset})
        except suntime.SunTimeException as e:
            continue
        if sunset < sunrise:
            day[place["name"]] = date
    times.sort(key=lambda time: time["time"])
    for time in times:
        if time["type"] == "sunrise":
            day[time["name"]] = time["time"]
        if time["type"] == "sunset":
            del(day[time["name"]])
            if len(day) == 0:
                print(f"{time['name']} {time['type']} {time['time']}")
                exit(0)
    date += one_day

