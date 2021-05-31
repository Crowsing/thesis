from input_validation.additional_diseases_validation import additional_diseases_validation
from input_validation.additional_symptoms_validation import additional_symptoms_validation
from input_validation.age_validation import age_validation
from input_validation.body_temperature_validation import body_temperature_validation
from input_validation.contact_with_an_infected_in_last_14_days_validation import \
    contact_with_an_infected_in_last_14_days_validation
from input_validation.gender_validation import gender_validation
from input_validation.main_symptoms_validation import main_symptoms_validation
from input_validation.suggestive_questions_validation import suggestive_questions_validation


def validation(
        sex: str,
        age: int,
        additional_diseases: list,
        main_symptoms: list,
        additional_symptoms: list,
        suggestive_questions: list,
        body_temperature: str,
        contact_with_an_infected_in_last_14_days: str
):
    """
    Валіданія усіх вхідних даних
    :param sex: str
    :param age: int
    :param additional_diseases: list
    :param main_symptoms: list
    :param additional_symptoms: list
    :param suggestive_questions: list
    :param body_temperature: str
    :param contact_with_an_infected_in_last_14_days: str
    :return: boolean
    """
    if age_validation(age) and \
            additional_diseases_validation(additional_diseases) and \
            additional_symptoms_validation(additional_symptoms) and \
            body_temperature_validation(body_temperature) and \
            contact_with_an_infected_in_last_14_days_validation(contact_with_an_infected_in_last_14_days) and \
            gender_validation(sex) and \
            main_symptoms_validation(main_symptoms) and \
            suggestive_questions_validation(suggestive_questions):
        return True
    return False
