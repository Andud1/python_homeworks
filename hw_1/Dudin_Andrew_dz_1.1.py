duration = int(input('Enter duration: '))

if duration < 60:
    print(duration, 'Секунд')

elif duration >= 60 and duration < 3600:
    duration_converted_min = duration // 60
    duration_converted_sec = duration % 60
    if duration_converted_sec == 0:
        print(duration_converted_min, 'Минут')
    else:
        print(duration_converted_min, 'Минут,', duration_converted_sec, 'Секунд')

elif duration >= 3600 and duration < 86400:
    duration_converted_hours = duration // 3600
    duration_converted_min = (duration % 3600) // 60
    duration_converted_sec = (duration % 3600) % 60
    if duration_converted_min == 0 and duration_converted_sec == 0:
        print(duration_converted_hours, 'Часов')
    elif duration_converted_min == 0 and duration_converted_sec != 0:
        print(duration_converted_hours, ',', duration_converted_sec, 'секунд')
    elif duration_converted_min != 0 and duration_converted_sec == 0:
        print(duration_converted_hours, 'Часов,', duration_converted_min, 'минут')
    else:
        print(duration_converted_hours, 'Часов,', duration_converted_min, 'минут,', duration_converted_sec, 'секунд')

else:
    duration_converted_days = duration // 86400
    duration_converted_hours = (duration % 86400) // 3600
    duration_converted_min = ((duration % 86400) % 3600) // 60
    duration_converted_sec = ((duration % 86400) % 3600) % 60
    if duration_converted_min == 0 and duration_converted_sec == 0 and duration_converted_hours == 0:
        print(duration_converted_days, 'Дней')

    elif duration_converted_min == 0 and duration_converted_sec != 0 and duration_converted_hours == 0:
        print(duration_converted_days, 'Дней,', duration_converted_sec, 'секунд')

    elif duration_converted_min == 0 and duration_converted_sec != 0 and duration_converted_hours == 0:
        print(duration_converted_days, 'Дней,', duration_converted_sec, 'секунд')

    elif duration_converted_min != 0 and duration_converted_sec == 0 and duration_converted_hours != 0:
        print(duration_converted_days, 'Дней,', duration_converted_hours, 'часов,', duration_converted_min, 'минут')

    elif duration_converted_min != 0 and duration_converted_sec != 0 and duration_converted_hours == 0:
        print(duration_converted_days, 'Дней,', duration_converted_min, 'минут,', duration_converted_sec, 'секунд')

    elif duration_converted_min == 0 and duration_converted_sec != 0 and duration_converted_hours != 0:
        print(duration_converted_days, 'Дней,', duration_converted_hours, 'часов,', duration_converted_sec, 'секунд')

    elif duration_converted_hours == 0 and duration_converted_sec == 0 and duration_converted_min != 0:
        print(duration_converted_days, 'Дней,', duration_converted_min, 'минут')

    elif duration_converted_min == 0 and duration_converted_sec == 0 and duration_converted_hours != 0:
        print(duration_converted_days, 'Дней,', duration_converted_hours, 'часов')

    else:
        print(duration_converted_days, 'Дней,', duration_converted_hours, 'Часов,', duration_converted_min, 'минут,', duration_converted_sec, 'секунд')

