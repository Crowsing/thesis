"""
Приклад використання
змінна sex приймає рядок 'man' або 'woman'
змінна age приймає будь яке ціле число в діапазоні 0 - 120
змінна additional_diseases приймає список додаткових симптомів, що перераховані в data.py
змінна main_symptoms приймає список симптомів, що перераховані в data.py
змінна suggestive_questions приймає список питань на які пацієнт відповів "ТАК", що перераховані в data.py
змінна body_temperature приймає рядок який є діапазоном температури, шо перерахована в data.py. \
Неможливо вказати діапазон, якщо не має симптому "Висока температура тіла"
змінна contact_with_an_infected_in_last_14_days приймає один із рядків contact_with_an_infected_in_last_14_days з data.py

"""

from calculating_a_recommendation import calculating_a_recommendation

sex = 'man'
age = 20
additional_diseases = []
main_symptoms = []
additional_symptoms = []
suggestive_questions = []
body_temperature = ''
contact_with_an_infected_in_last_14_days = 'Нічого з перерахованого вище'

if __name__ == '__main__':
    print(calculating_a_recommendation(
        sex,
        age,
        additional_diseases,
        main_symptoms,
        additional_symptoms,
        suggestive_questions,
        body_temperature,
        contact_with_an_infected_in_last_14_days
    ))

