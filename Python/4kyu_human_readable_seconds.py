# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    if seconds == 0:
        return "now"
    time = []
    while seconds != 0:
        if seconds // (365*24*60*60):
            time.append(str(seconds // (365*24*60*60)) + (" year" if seconds // (365*24*60*60) == 1 else " years"))
            seconds -= (seconds // (365*24*60*60)) * (365*24*60*60)
        elif seconds // (24*60*60):
            time.append(str(seconds // (24*60*60)) + (" day" if seconds // (24*60*60) == 1 else " days"))
            seconds -= (seconds // (24*60*60)) * (24*60*60)
        elif seconds // (60*60):
            time.append(str(seconds // (60*60)) + (" hour" if seconds // (60*60) == 1 else " hours"))
            seconds -= (seconds // (60*60)) * (60*60)
        elif seconds // 60:
            time.append(str(seconds // 60) + (" minute" if seconds // (60) == 1 else " minutes"))
            seconds -= (seconds // 60) * 60
        else:
            time.append(str(seconds) + (" second" if seconds == 1 else " seconds"))
            seconds = 0
    return ", ".join(time[:-1]) + " and " + time[-1] if len(time) > 1 else "".join(time)
