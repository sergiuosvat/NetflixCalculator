ok = "yes"
while ok == "yes":
    total_hours = int(input("Total hours: "))
    total_minutes = int(input("Total minutes: "))
    total_seconds = int(input("Total seconds: "))

    remaining_hours = int(input("Remaining hours: "))
    remaining_minutes = int(input("Remaining minutes: "))
    remaining_seconds = int(input("Remaining seconds: "))

    if remaining_seconds > total_seconds:
        total_seconds = total_seconds + 60
        total_minutes = total_minutes - 1
        if total_minutes == 0:
            minutes = total_minutes + 59
            hours = total_hours - 1
            seconds = total_seconds - remaining_seconds
        else:
            minutes = total_minutes - remaining_minutes
            seconds = total_seconds - remaining_seconds
    else:
        seconds = total_seconds - remaining_seconds

    if remaining_minutes > total_minutes:
        total_minutes = total_minutes + 60
        total_hours = total_hours - 1
        if total_hours == 0:
            hours = 0
        else:
            hours = total_hours
        minutes = total_minutes - remaining_minutes
    else:
        hours = total_hours - remaining_hours
        minutes = total_minutes - remaining_minutes

    print("Current time: {}:{}':{}''".format(hours, minutes, seconds))
    print("Current hours: ", hours)
    if minutes < 10:
        print("Current minutes: 0{}".format(minutes))
    else:
        print("Current minutes ", minutes)
    if seconds < 10:
        print("Current seconds: 0{}".format(seconds))
    else:
        print("Current seconds: ", seconds)
    print("Again?")
    ok = input("yes/no: ")
