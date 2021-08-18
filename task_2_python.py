from result_df import add_new_contractor, T_CONTRACTOR_WORK_DAY
from feature_df import df

# Задание 3
# Создать процедуру расчета рабочих дней.

add_new_contractor(df)
T_CONTRACTOR_WORK_DAY.to_csv('~/PycharmProjects/magnit/T_CONTRACTOR_WORK_DAY.csv', index=False)
print(T_CONTRACTOR_WORK_DAY)

#Задание 4
# Сделать выборку, содержащую, сколько рабочих дней было у каждого поставщика
# Сделать выборку поставщиков, у которыйх было больше 10 рабочих дней за январь 2019 года
# Сделать выборку поставщиков, кто работал 14, 15 и 16 января 2019 года









