import decimal

import data


def age(age_value: int):
    for age_range in data.ages:
        if int(age_range.split(', ')[0]) <= age_value < int(age_range.split(', ')[1]):
            return data.ages[age_range]


def health_rate(additional_diseases: list):
    health_problem_rate = 1
    for additional_diagnosis in additional_diseases:
        health_problem_rate += decimal.Decimal(data.additional_diseases[additional_diagnosis])
    return health_problem_rate


def main_symptom(main_symptoms: list):
    symptom_score = 0
    if main_symptoms:
        for symptom in main_symptoms:
            symptom_score += data.main_symptoms[symptom]
    return symptom_score


def additional_symptom(additional_symptoms: list):
    symptom_score = 0
    if additional_symptoms:
        for symptom in additional_symptoms:
            symptom_score += data.additional_symptoms[symptom]
    return symptom_score


def questions(suggestive_questions: list):
    symptom_score = 0
    if suggestive_questions:
        for suggestive_question in suggestive_questions:
            symptom_score += data.suggestive_questions[suggestive_question]
    return symptom_score


def result(gender_rate, age_rate, health_problem_rate, symptom_score):
    return float(decimal.Decimal(gender_rate) + \
                 decimal.Decimal(age_rate) + \
                 decimal.Decimal(health_problem_rate)) * symptom_score


def high_fever(main_symptoms: list, body_temperature: str):
    symptom_score = 0
    if 'Висока температура тіла' in main_symptoms:
        symptom_score += data.body_temperature[body_temperature]
    return symptom_score


def contact_with_the_sick(contact_with_an_infected_in_last_14_days: str):
    if contact_with_an_infected_in_last_14_days == 'Нічого з перерахованого вище':
        return data.result['okay']
    else:
        return data.result['have_contact_with_covid']