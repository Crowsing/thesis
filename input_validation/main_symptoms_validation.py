import data


def main_symptoms_validation(main_symptoms: list):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param main_symptoms: list
    :return: boolean
    """
    if not main_symptoms:
        return True

    for main_symptom in main_symptoms:
        if main_symptom not in data.main_symptoms:
            return False

    return True
