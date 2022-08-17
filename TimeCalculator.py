
def add_time(start, duration, day=''):
    start_format = start.split(' ')[1]
    start = start[:-2]
    start_hour = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1])
    timer_minutes = int(duration.split(':')[1])
    timer_hours = int(duration.split(':')[0])

    days = {
        '0': 'Monday',
        '1': 'Tuesday',
        '2': 'Wednesday',
        '3': 'Thursday',
        '4': 'Friday',
        '5': 'Saturday',
        '6': 'Sunday'
    }
    inv_days = {v: k for k, v in days.items()}

    # adding minutes
    passed_days = 0
    if start_minutes+timer_minutes <= 59:
        end_minutes = start_minutes+timer_minutes
        end_hour = start_hour
    else:
        end_minutes = timer_minutes-(59-start_minutes)-1
        end_hour = start_hour + 1
        if end_hour == 12:
            if start_format == 'AM':
                start_format = 'PM'
            elif start_format == 'PM':
                start_format = 'AM'
                passed_days += 1
        if end_hour == 13:
            end_hour == 1

    # adding hours
    i = 0
    for i in range(0, timer_hours):
        if end_hour == 13:
            end_hour = 1
        end_hour += 1

        if end_hour == 12:
            if start_format == 'AM':
                start_format = 'PM'
            elif start_format == 'PM':
                start_format = 'AM'
                passed_days += 1
    # converting back to strings
    end_minutes = str(end_minutes)
    if len(end_minutes) == 1:
        end_minutes = '0'+end_minutes
    end_hour = str(end_hour)
    end_format = str(start_format)
    l = end_hour+':'+end_minutes+' '+end_format
   # format
    if day is add_time.__defaults__[0]:
        if passed_days == 1:
            l = end_hour+':'+end_minutes+' '+end_format+' (next day)'
        elif passed_days > 1:
            l = end_hour+':'+end_minutes+' ' + \
                end_format + f' ({passed_days} days later)'
        day = 1
    else:
        day = day.lower().capitalize()
        start_day = inv_days.get(day)
        end_day = days.get(str(((int(start_day)+passed_days)) % 7))
        print(start_day)
        if passed_days == 0:
            l = end_hour+':'+end_minutes+' ' + end_format + f', {day}'
        if passed_days == 1:
            l = end_hour+':'+end_minutes+' ' + \
                end_format + f', {end_day} (next day)'
        if passed_days > 1:
            l = end_hour+':'+end_minutes+' ' + end_format + \
                f', {end_day} ({passed_days} days later)'

    new_time = l
    return new_time


print(add_time("2:59 AM", "24:00", "saturDay"))
