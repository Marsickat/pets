import datetime as dt

vlad_birthday = dt.date(1996, 10, 9)  # День рождения Влада
igor_birthday = dt.date(1998, 6, 28)  # День рождения Игоря

today = dt.date.today()  # Получение сегодняшней даты
today_year = today.year  # Получение текущего года

# Заменяем текущие значения года в днях рождения
vlad_birthday = vlad_birthday.replace(year=today_year)
igor_birthday = igor_birthday.replace(year=today_year)

vlad_days_left = vlad_birthday - today
igor_days_left = igor_birthday - today

print(vlad_days_left.days, igor_days_left.days, sep="\n")
