class Road:
    _mass = 25
    _thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return f"{self._length * self._width * self._mass * self._thickness} кг"


r = Road(20, 5000)
print(r.calc())