import pandas as pd
from datetime import datetime

df = pd.read_csv(r'shedulers.csv', encoding='cp1251', sep=';')
df['ID'] = df.index+1
#### по всей видимости 9999 год  означает, что смены продолжаются по н/в
df.loc[df['Дата окончания расписания'] == '31.12.9999 0:00',
       'Дата окончания расписания'] = datetime.now().strftime("%d.%m.%Y %H:%M")
df["month"] = df['Дата начала расписания'].map(lambda x: x[:2])
df["day"] = df['Дата начала расписания'].map(lambda x: x[3:5])
df["year"] = df['Дата начала расписания'].map(lambda x: x[6:10])
df['Дата начала расписания'] = \
    (df['day'] +'.'+df['month'] +'.'+  df['year']).astype('datetime64[s]')

df["month"] = df['Дата окончания расписания'].map(lambda x: x[:2])
df["day"] = df['Дата окончания расписания'].map(lambda x: x[3:5])
df["year"] = df['Дата окончания расписания'].map(lambda x: x[6:10])

df['Дата окончания расписания'] = \
    (df['day'] +'.'+df['month'] +'.'+  df['year']).astype('datetime64[s]')
df = df.drop(['month', 'day', 'year'], axis=1)