import decimal

import pandas as pd


sex = {'male': 0, 'female': 0}
ages = {
    '0, 10': 0,
    '10, 20': 0,
    '20, 30': 0,
    '30, 40': 0,
    '40, 50': 0,
    '50, 60': 0,
    '60, 70': 0,
    '70, 120': 0
}
df = pd.read_csv("data/COVID19_open_line_list.csv", low_memory=False)

# sex
for gender in df['sex'].dropna():
    if gender in sex.keys():
        sex[gender] += 1

all_count = sex['male'] + sex['female']
man = float(decimal.Decimal((sex['male'] * 100) / all_count))
woman = float(decimal.Decimal((sex['female'] * 100) / all_count))


# ages

for age in df['age'].dropna():
    if age.isdigit():
        if 0 <= int(age) < 10:
            ages['0, 10'] += 1
        elif 10 <= int(age) < 20:
            ages['10, 20'] += 1
        elif 20 <= int(age) < 30:
            ages['20, 30'] += 1
        elif 30 <= int(age) < 40:
            ages['30, 40'] += 1
        elif 40 <= int(age) < 50:
            ages['40, 50'] += 1
        elif 50 <= int(age) < 60:
            ages['50, 60'] += 1
        elif 60 <= int(age) < 70:
            ages['60, 70'] += 1
        elif 70 <= int(age) < 120:
            ages['70, 120'] += 1


all_ages = 0

for age in ages:
    all_ages += ages[age]

# result
proc_ages = {}

for age in ages:
    proc_ages[age] = float(decimal.Decimal((ages[age] * 100) / all_ages))

print(man, woman)
print(proc_ages)
