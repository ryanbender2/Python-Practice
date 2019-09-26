""" Jake's Meal Time
  Jake is a very habitual person.
  He eats breakfast at 7:00 a.m.
  each morning, lunch at 12:00 p.m.
  and dinner at 7:00 p.m. in the evening.

  Create a function that takes in the current
  time as a string and determines the duration
  of time before Jake's next meal. Represent
  this as a list with the first and second
  elements representing hours and minutes,
  respectively.
"""


def time_to_eat(current_time):
    time, THC = current_time.split()
    hr, minute = time.split(':')
    if THC[0] == 'p':
        time24 = str(int(hr) + 12) + ':' + minute
    else:
        time24 = time
    hr_24, minute_24 = time24.split(':')
    time_in_minutes = (int(hr_24) * 60) + int(minute_24)
    if time_in_minutes < 420:  # (*_*)
        tte_hr = int((420 - time_in_minutes) / 60)
        tte_min = abs((time_in_minutes % 60) - 60)
        if tte_min == 60:
            tte_min = 0
        return [tte_hr, tte_min]
    if time_in_minutes < 720:
        tte_hr = int((720 - time_in_minutes) / 60)
        tte_min = abs((time_in_minutes % 60) - 60)
        if tte_min == 60:
            tte_min = 0
        return [tte_hr, tte_min]
    if time_in_minutes < 1140:
        tte_hr = int((1140 - time_in_minutes) / 60)
        tte_min = abs((time_in_minutes % 60) - 60)
        if tte_min == 60:
            tte_min = 0
        return [tte_hr, tte_min]
    if time_in_minutes > 1139:
        tte_hr = int((1440 - time_in_minutes) / 60) + 7
        tte_min = abs((time_in_minutes % 60) - 60)
        if tte_min == 60:
            tte_min = 0
        return [tte_hr, tte_min]


print(time_to_eat("8:01 p.m."))
