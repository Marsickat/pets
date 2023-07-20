import math


class Planet:
    def __init__(self, name: str, radius: float, temp_celsius: float):
        """
        Создает новый объект класса Planet.

        :param name: Название планеты.
        :type name: str
        :param radius: Радиус планеты (км).
        :type radius: float
        :param temp_celsius: Температура планеты (по Цельсию).
        :type temp_celsius: float
        """
        self.name = name
        self.surface_area = 4 * math.pi * radius * radius  # Площадь поверхности планеты (км**2)
        self.average_temp_celsius = temp_celsius  # Средняя температура поверхности планеты по Цельсию
        self.average_temp_fahrenheit = temp_celsius * 9 / 5 + 32  # Средняя температура поверхности планеты по Фаренгейту

    def show_info(self) -> None:
        """
        Выводит информацию о планете.
        """
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit} градусов по Фаренгейту.")


jupiter = Planet("Юпитер", 69911, -108)

jupiter.show_info()
