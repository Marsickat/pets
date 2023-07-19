WEIGHT = 75  # Вес (кг)
HEIGHT = 175  # Рост (см)
K_1 = 0.035  # Коэффициент для подсчета калорий
K_2 = 0.029  # Коэффициент для подсчета калорий
STEP_M = 0.65  # Длина шага (м)
TRANSFER_COEFF = 1000  # Коэффициент перевода из м в км

storage_data = {}  # Словарь для хранения полученных данных


def accept_package(time: str, steps: int) -> dict:
    """Принимает данные о времени и количестве шагов и выполняет следующие действия:

    1. Проверяет корректность входных данных с помощью функции `check_correct_data`.
    2. Получает количество пройденных дней с помощью функции `get_step_days`.
    3. Вычисляет пройденное расстояние в километрах с помощью функции `get_distance`.
    4. Записывает значение количества шагов в хранилище данных `storage_data` по соответствующему времени.
    5. Вычисляет количество потраченных килокалорий с помощью функции `get_spent_calories`.
    6. Получает мотивирующее сообщение на основе пройденного расстояния с помощью функции `get_achievement`.
    7. Выводит информацию о времени, количестве шагов, пройденном расстоянии и потраченных килокалориях.

    :param time: Время запроса
    :type time: str
    :param steps: Кол-во шагов
    :type steps: int
    :return: Словарь storage_dict
    :rtype: dict
    """
    if check_correct_data((time, steps)):
        steps = get_step_days(steps)  # Получение количества пройденных шагов
        dist = get_distance(steps)  # Вычисление пройденного расстояния в км
        storage_data[time] = steps  # Запись значения
        spent_calories = get_spent_calories(dist, time)  # Вычисление кол-ва потраченных килокалорий
        achievement = get_achievement(dist)  # Получение мотивирующего сообщения
        output = f"Время: {time}.\nКоличество шагов за сегодня: {steps}.\nДистанция составила: {dist} км.\nВы сожгли {spent_calories} ккал.\n{achievement}"
        print(output)
    return storage_data


def check_correct_data(data: tuple) -> bool:
    """Проверяет корректность входных данных

    :param data: Кортеж с данными в виде (<время>, <кол-во шагов>)
    :type data: tuple
    :return: Результат проверки. Если кортеж состоит из двух элементов и оба элемента не None, то True, иначе False
    :rtype: bool
    """
    return len(data) == 2 and data[0] and data[1] and check_correct_time(data[0])


def check_correct_time(time: str) -> bool:
    """Проверяет корректность времени

    :param time: Время запроса
    :type time: str
    :return: Результат проверки. Если предыдущее записанное значение меньше, чем время запроса, или отсутствует, то True, иначе False
    :rtype: bool
    """
    time = tuple(map(int, time.split(":")))
    if storage_data.keys():
        last_time = tuple(map(int, tuple(storage_data.keys())[-1].split(":")))
        return last_time <= time
    return not storage_data


def get_step_days(steps: int) -> int:
    """Возвращает количество пройденных шагов за день

    :param steps: Количество шагов, сделанных с момента последнего запроса
    :type steps: int
    :return: Количество пройденных шагов за день
    :rtype: int
    """
    for steps_count in storage_data.values():
        steps += steps_count
    return steps


def get_distance(steps: int) -> float:
    """Переводит количество пройленных шагов в количество пройденных километров

    :param steps: Количество пройденных шагов
    :type steps: int
    :return: Количество пройденных километров
    :rtype: float
    """
    return round(steps * STEP_M / TRANSFER_COEFF, 2)


def get_spent_calories(dist: float, current_time: str) -> float:
    """Вычисляет количество потраченных килокалорий (согласно формуле Южного Методистского университета в Далласе)

    :param dist: Количество пройденных километров
    :type dist: float
    :param current_time: Значение затраченного времени
    :type current_time: str
    :return: Количество потраченных килокалорий
    :rtype: float
    """
    current_time = current_time.split(":")
    speed = round(dist / ((int(current_time[0]) * 60 + int(current_time[1])) / 60), 2)
    mins = round((int(current_time[0]) * 60 + int(current_time[1]) + int(current_time[2]) / 60), 2)
    return round((K_1 * WEIGHT + speed ** 2 / HEIGHT * (K_2 * WEIGHT)) * mins)


def get_achievement(dist: float) -> str:
    """Возвращает мотивирующее сообщение, основываясь на кол-ве пройденного расстояния

    :param dist: Количество пройденных километров
    :type dist: float
    :return: Мотивирующее сообщение
    :rtype: str
    """
    if dist > 6.5:
        achievement = "Отличный результат! Цель достигнута."
    elif dist > 3.9:
        achievement = "Неплохо! День был продуктивным."
    elif dist > 2:
        achievement = "Маловато, но завтра наверстаем!"
    else:
        achievement = "Лежать тоже полезно. Главное - участие, а не победа!"
    return achievement


time = "9:36:02"  # Входное время
steps = 15302  # Входное кол-во шагов
accept_package(time, steps)  # Обрабатываем входные данные

time = "15:45:12"
steps = 5000
accept_package(time, steps)

time = "10:45:12"
steps = 5000
accept_package(time, steps)
