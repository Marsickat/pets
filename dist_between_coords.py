from math import sin, cos, acos


class Point:
    def __init__(self, latitude: float, longitude: float):
        """
        Создает объект класса Point.

        :param latitude: Широта.
        :type latitude: float
        :param longitude: Долгота.
        :type longitude: float
        """
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, other: "Point") -> float:
        """
        Считает расстояние между двумя точками в км.

        :param other: Вторая точка.
        :type other: Point
        :return: Расстояние между двумя точками
        :rtype: float
        """
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
            self.longitude - other.longitude)
        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude: float, longitude: float, name: str, population: int):
        """
        Создает объект класса City.

        :param latitude: Широта.
        :type latitude: float
        :param longitude: Долгота.
        :type longitude: float
        :param name: Название города.
        :type name: str
        :param population: Население города.
        :type population: int
        """
        self.name = name
        self.population = population
        super().__init__(latitude, longitude)


class Mountain(Point):
    def __init__(self, latitude: float, longitude: float, name: str, height: int):
        """
        Создает объект класса City.

        :param latitude: Широта.
        :type latitude: float
        :param longitude: Долгота.
        :type longitude: float
        :param name: Название горы.
        :type name: str
        :param height: Высота горы.
        :type height: int
        """
        self.name = name
        self.height = height
        super().__init__(latitude, longitude)

    def show(self):
        """
        Выводит информацию о горе.
        """
        print(f"Название: {self.name} || Высота: {self.height} || Широта: {self.latitude} || Долгота: {self.longitude}")


Moscow = City(55.755864, 37.755864, "Москва", 13_104_177)
Everest = Mountain(27.9880619, 86.9252853, "Эверест", 8848)

Everest.show()

print(Moscow.distance(Everest))
