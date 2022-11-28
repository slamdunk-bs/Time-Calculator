def add_time(start, duration, date=False):

    date_change = 0
    time1 = start.split(" ")
    time2 = time1[0].split(":")
    time_add = duration.split(":")

    time_hour = int(time2[0]) + int(time_add[0])
    time_min = int(time2[1]) + int(time_add[1])
     
    if time_min > 60:
        time_min -= 60
        time_hour += 1
    if time_min < 10:
        time_min = "0" + str(time_min)

    change_ampm = ['AM', 'PM']
    if time_hour > 11:
        if time_hour > 24:
            while time_hour > 24:
                time_hour -= 24
                date_change += 1
            if time_hour > 12:
                if time1[1] == 'AM':
                    time_hour -= 12
                    time1[1] = 'PM'
                else:
                    time_hour -= 12
                    time1[1] = 'AM'
                    date_change += 1
        if time_hour > 12:
                if time1[1] == 'AM':
                    time_hour -= 12
                    time1[1] = 'PM'
                else:
                    time_hour -= 12
                    time1[1] = 'AM'
                    date_change += 1
        if time_hour > 11:
            if time1[1] == 'AM':
                time1[1] = 'PM'
            else:
                time1[1] = 'AM'
                date_change += 1

    if date is False:
        if date_change == 1:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1] + " (next day)"
        elif date_change > 1:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1] + " (" + str(date_change) + " days later)"
        else:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1]
        return new_time  

    else:
        day_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        date = date.capitalize()
        day = day_week[(day_week.index(date) + date_change) % 7]
        if date_change == 1:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1] + ", " + day + " (next day)"
        elif date_change > 1:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1] + ", " + day + " (" + str(date_change) + " days later)"
        else:
            new_time = str(time_hour) + ":" + str(time_min) + " " + time1[1] + ", " + day
        return new_time
