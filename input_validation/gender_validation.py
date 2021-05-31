def gender_validation(sex: str):
    """
    Перевірка корректності даних про стать пацієнта
    :param sex: str
    :return: boolean
    """
    if sex == 'man' or sex == 'woman':
        return True
    return False
