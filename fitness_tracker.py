weight = 75  # Вес
height = 175  # Рост
steps = 8462  # Количество пройденных шагов за день
hours = 2  # Время движения (ч)
len_step_m = 0.65  # Длина одного шага (м)
transfer_coeff = 1000  # Коэффициент перевода из м в км

dist = steps * len_step_m / transfer_coeff  # Вычисление пройденного расстояния (км)
speed = dist / hours  # Вычисление средней скорости движения (км/ч)
mins = hours * 60  # Перевод из часов в минуты

spent_calories = (0.035 * weight + speed ** 2 / height * (
        0.029 * weight)) * mins  # Вычисление количества потраченных килокалорий (согласно формуле Южного Методистского университета в Далласе)

output = str(dist) + " " + str(spent_calories)
print(output)
