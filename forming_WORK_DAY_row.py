from datetime import timedelta

work_day_dict = {'д': [8, 12, 4], 'н': [20, 12, 16],'с': [8, 24, 16]}

def forming_WORK_DAY_row(row_schedule, start_second_day,
                            T_CONTRACTOR_WORK_DAY_row, df_schedule_id, df, end_days):

    for work_day in row_schedule:

        if work_day in work_day_dict:
            start_current_day = start_second_day + \
                                timedelta(hours = work_day_dict[work_day][0])
            end_current_day = start_current_day + \
                              timedelta(hours = work_day_dict[work_day][1])
            start_second_day = end_current_day + \
                               timedelta(hours = work_day_dict[work_day][2])
            T_CONTRACTOR_WORK_DAY_row.append([df[df.ID==df_schedule_id]['ФИО'].tolist(),
                               start_current_day, end_current_day])
        else:
            start_second_day = start_second_day + timedelta(days = 1)

        if start_second_day > end_days:
            break

    return T_CONTRACTOR_WORK_DAY_row, start_second_day
