from time import sleep

class TrafficLight:
    __traffic_states = {"red": 7, "yellow": 2, "green": 4}
    __color = ""

    def running(self):
        for k in self.__traffic_states:
            self.__color = k
            print(f"Цвет: {self.__color}")
            sleep(self.__traffic_states[k])