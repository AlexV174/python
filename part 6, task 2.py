class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__height = 5
        self.__weight_m = 25

    def calculate_weight(self):
        return self._length * self._width * self.__weight_m * self.__height


road = Road(5000, 20)

print(f"{road.calculate_weight() / 1000} т")
