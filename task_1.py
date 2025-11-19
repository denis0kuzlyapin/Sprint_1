minutes = 0
string = '1h 45m,360s,25m,30m 120s,2h 60s'

string_off_comma = string.replace(',', ' ')  # Убираем запятые

time_values = string_off_comma.split(' ')  # Разбиваем на подстроки по пробелу


for v in time_values:
    if 'h' in v:
        hours = int(v[:-1]) * 60  # Отбрасываем 'h'и переводим часы в минуты
        minutes += hours
    elif 's' in v:
        # Отбрасываем 's'и переводим секунды в минуты
        seconds = int(v[:-1]) / 60
        minutes += seconds
    elif 'm' in v:
        # Отбрасываем 'm' и оставляем только количество минут
        minutes += int(v[:-1])

print(int(minutes))  # Выводим количество минут (целочисленное — int)
