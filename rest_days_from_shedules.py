from first_day_from_shedule import work_day_dict
from datetime import timedelta

def rest_cycle_shedule_days(shedule, start_second_day, id_shedule, id_shed, df, end_days):

    for work_day in shedule:

        if work_day in work_day_dict:
            start_current_day = start_second_day + \
                                timedelta(hours = work_day_dict[work_day][0])
            end_current_day = start_current_day + \
                              timedelta(hours = work_day_dict[work_day][1])
            start_second_day = end_current_day + \
                               timedelta(hours = work_day_dict[work_day][2])
            id_shedule.append([df[df.ID==id_shed]['ФИО'].tolist(),
                               start_current_day, end_current_day])
        else:
            start_second_day = start_second_day + timedelta(days = 1)

        if start_second_day > end_days:
            break

    return id_shedule, start_second_day
