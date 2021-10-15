class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула: {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print("Скорость превышена")


class SportCar(Car):
    def f():
        return


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print("Скорость превышена")


class PoliceCar(Car):
    def f():
        return


c = WorkCar(90, "red", "bmw", False)
c.show_speed()
