import datetime as dt

FORMAT = "%d.%m.%Y"


def get_days_to_birthday(name: str, date_birthday: str) -> str:
    """Получает имя и дату дня рождения и возвращает строку с информацией о количестве оставшихся дней до дня рождения.

    :param name: Имя
    :type name: str
    :param date_birthday: Дата дня рождения
    :type date_birthday: str
    :return: Строка с информацией о количестве дней оставшихся дней до дня рождения
    :rtype: str
    """
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT).date()  # Перевод даты из строки в объект date

    today = dt.date.today()  # Получение сегодняшней даты
    today_year = today.year  # Получение текущего года
    date_birthday = date_birthday.replace(year=today_year)  # Заменяем текущее значение года в дне рождения

    # Проверка на уже прошедший в этом году день рождения
    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today_year + 1)
        days_left = (date_birthday - today).days
    else:
        days_left = (date_birthday - today).days

    return f"{name}, до твоего дня рождения осталось дней: {days_left}"


data = [("Влад", "9.10.1996"), ("Игорь", "28.6.1998"), ("Кирилл", "2.7.1998")]

for name, birthday in data:
    print(get_days_to_birthday(name, birthday))
