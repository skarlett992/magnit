from one_id_schedule import one_id_schedule
import pandas as pd

T_CONTRACTOR_WORK_DAY = pd.DataFrame(columns=['ID', 'NAME', 'DATE_BEGIN', 'DATE_END'])

def add_new_contractor(df):

    for df_schedule_id in df['ID']:
        start_days = df[df.ID == df_schedule_id]['Дата начала расписания'].tolist()[0]
        end_days = df[df.ID == df_schedule_id]['Дата окончания расписания'].tolist()[0]
        row_schedule = df[df.ID == df_schedule_id]['Расписание'].tolist()[0]

        T_CONTRACTOR_WORK_DAY_row = one_id_schedule(start_days,
                                    end_days,
                                    row_schedule,
                                    df_schedule_id,
                                    df)

        for row in T_CONTRACTOR_WORK_DAY_row:
            df_len = T_CONTRACTOR_WORK_DAY.shape[0]
            T_CONTRACTOR_WORK_DAY.loc[df_len] = [
                df_len+1, row[0][0], row[1], row[2]
            ]


