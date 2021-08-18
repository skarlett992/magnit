from forming_WORK_DAY_row import forming_WORK_DAY_row

def one_id_schedule(start_days, end_days,
                    row_schedule, df_schedule_id, df):
    T_CONTRACTOR_WORK_DAY_row = []

    start_second_day = start_days
    while start_second_day <= end_days:

        T_CONTRACTOR_WORK_DAY_row, start_second_day = forming_WORK_DAY_row(
            row_schedule,
            start_second_day,
            T_CONTRACTOR_WORK_DAY_row,
            df_schedule_id,
            df,
            end_days)


    return T_CONTRACTOR_WORK_DAY_row