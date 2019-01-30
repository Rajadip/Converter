
def toSec(hours):
    hours = hours.split(':')
    if len(hours) == 3:
        return (float(hours[0]) * 60 * 60) + (float(hours[1]) * 60) + float(hours[2])
    elif len(hours) == 2:
        return (float(hours[0]) * 60) + (float(hours[1]))
    elif len(hours) == 1:
        return float(hours[0])
