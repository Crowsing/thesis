def age_validation(age: int):
    """
    Перевірка корректності даних про вік пацієнта
    :param age: int
    :return: boolean
    """
    if 0 <= age <= 120:
        return True
    return False
