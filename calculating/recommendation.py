from input_validation.validation import validation
import data
import calculating.calculating as calc


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
        health_problem_rate = calc.health_rate(additional_diseases)
        # коефіцієнт проблем зі здоров\'ям
        age_rate = int
        # коефіцієнт пов\'язаний з віком

        age_rate = calc.age(age)

        symptom_score = calc.main_symptom(main_symptoms)

        symptom_score += calc.additional_symptom(additional_symptoms)

        if symptom_score == 0:
            return calc.contact_with_the_sick(contact_with_an_infected_in_last_14_days)
        else:
            symptom_score += calc.high_fever(main_symptoms, body_temperature)

            symptom_score += calc.questions(suggestive_questions)

            result = calc.result(gender_rate, age_rate, health_problem_rate, symptom_score)

            if 0 < result <= 50:
                return data.result['some_problems']
            else:
                return data.result['big_problems']
    else:
        return 'Error validation'
