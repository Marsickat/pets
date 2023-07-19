import datetime as dt


def get_days_to_birthday(date_birthday: dt.date) -> int:
    """Получает дату дня рождения и возвращает количество оставшихся дней до этой даты.

    :param date_birthday: Дата дня рождения
    :type date_birthday: datetime.date
    :return: Количество оставшихся дней до дня рождения
    :rtype: int
    """
    today = dt.date.today()  # Получение сегодняшней даты
    today_year = today.year  # Получение текущего года
    date_birthday = date_birthday.replace(year=today_year)  # Заменяем текущее значение года в дне рождения

    # Проверка на уже прошедший в этом году день рождения
    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today_year + 1)
        days_left = (date_birthday - today).days
    else:
        days_left = (date_birthday - today).days

    return days_left


vlad_birthday = dt.date(1996, 10, 9)  # День рождения Влада
igor_birthday = dt.date(1998, 6, 28)  # День рождения Игоря


print(get_days_to_birthday(vlad_birthday), get_days_to_birthday(igor_birthday), sep="\n")
