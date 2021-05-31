import data


def additional_diseases_validation(additional_diseases: list):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param additional_diseases: list
    :return: boolean
    """
    if not additional_diseases:
        return True

    for additional_diagnosis in additional_diseases:
        if additional_diagnosis not in data.additional_diseases:
            return False

    return True

