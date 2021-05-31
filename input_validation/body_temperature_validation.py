import data


def body_temperature_validation(body_temperature: str):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param body_temperature: str
    :return: boolean
    """
    if body_temperature == '' or body_temperature in data.body_temperature:
        return True
    return False
