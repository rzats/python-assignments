from enum import Enum

class Direction (Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8
    
class Weather (object):
    def __init__ (self, temperature, wind_direction, wind_speed, humidity, rain):
        self.temperature = temperature
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.rain = rain

    # Used to print the values in the dictionary.
    def __repr__ (self):
        return str(vars(self))
    
weather = {
    "L'viv": {
        "temperature": 15,
        "wind_direction": Direction.NE,
        "wind_speed": 6,
        "humidity": 94,
        "rain": True
    },
    "Zhytomyr": Weather(20, Direction.NW, 5, 59, True),
    "Ternopil": Weather(16, Direction.E, 3, 90, False),
    "Odesa": Weather(20, Direction.N, 11, 68, False),
    "Kyiv": Weather(22, Direction.W, 6, 50, False)
}

print (weather)

temperatures = [value.temperature for key, value in weather.items()]
print (sum(temperatures) / len(temperatures))
