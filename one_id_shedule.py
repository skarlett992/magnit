from first_day_from_shedule import cycle_shedule_first_day
from rest_days_from_shedules import rest_cycle_shedule_days

def one_id_shedule(start_days, end_days, shedule, id_shed, df):
    id_shedule = []

    start_second_day = start_days
    while start_second_day <= end_days:

        # id_shedule, start_second_day, shedule = cycle_shedule_first_day(
        #     shedule,
        #     start_days,
        #     id_shed,
        #     df, end_days)

        id_shedule, start_second_day = rest_cycle_shedule_days(
            shedule,
            start_second_day,
            id_shedule,
            id_shed,
            df,
            end_days
    )


    return id_shedule