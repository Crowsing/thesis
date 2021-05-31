import data


def additional_symptoms_validation(additional_symptoms: list):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param additional_symptoms: list
    :return: boolean
    """
    if not additional_symptoms:
        return True

    for additional_symptom in additional_symptoms:
        if additional_symptom not in data.additional_symptoms:
            return False

    return True
