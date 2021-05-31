import decimal

from input_validation.validation import validation
import data


def calculating_a_recommendation(
        sex: str,
        age: int,
        additional_diseases: list,
        main_symptoms: list,
        additional_symptoms: list,
        suggestive_questions: list,
        body_temperature: str,
        contact_with_an_infected_in_last_14_days: str
):
    if validation(
            sex,
            age,
            additional_diseases,
            main_symptoms,
            additional_symptoms,
            suggestive_questions,
            body_temperature,
            contact_with_an_infected_in_last_14_days
    ):
        gender_rate = data.sex[sex]
        # коефіцієнт пов\'язаний з статтю
        health_problem_rate = 1
        # коефіцієнт проблем зі здоров\'ям
        age_rate = int
        # коефіцієнт пов\'язаний з віком

        for age_range in data.ages:
            if int(age_range.split(', ')[0]) <= age <= int(age_range.split(', ')[1]):
                age_rate = data.ages[age_range]
                break

        for additional_diagnosis in additional_diseases:
            health_problem_rate += decimal.Decimal(data.additional_diseases[additional_diagnosis])

        symptom_score = 0
        if main_symptoms:
            for symptom in main_symptoms:
                symptom_score += data.main_symptoms[symptom]

        if additional_symptoms:
            for symptom in additional_symptoms:
                symptom_score += data.additional_symptoms[symptom]

        if symptom_score == 0:
            if contact_with_an_infected_in_last_14_days == 'Нічого з перерахованого вище':
                return data.result['okay']
            else:
                return data.result['have_contact_with_covid']
        else:
            if 'Висока температура тіла' in main_symptoms:
                symptom_score += data.body_temperature[body_temperature]

            if suggestive_questions:
                for suggestive_question in suggestive_questions:
                    symptom_score += data.suggestive_questions[suggestive_question]

            result_rate = decimal.Decimal(gender_rate) + \
                          decimal.Decimal(age_rate) + \
                          decimal.Decimal(health_problem_rate)

            result_rate = float(decimal.Decimal(result_rate))

            result = symptom_score * result_rate
            if 0 < result <= 50:
                return data.result['some_problems']
            else:
                return data.result['big_problems']
    else:
        return 'Error validation'
