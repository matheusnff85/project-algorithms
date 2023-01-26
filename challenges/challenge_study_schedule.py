def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= target_time and period[1] >= target_time:
            counter += 1

    return counter
