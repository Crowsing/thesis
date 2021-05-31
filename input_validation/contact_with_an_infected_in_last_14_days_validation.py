import data


def contact_with_an_infected_in_last_14_days_validation(contact_with_an_infected_in_last_14_days: str):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param contact_with_an_infected_in_last_14_days: str
    :return: boolean
    """
    if contact_with_an_infected_in_last_14_days == '' or \
            contact_with_an_infected_in_last_14_days in data.contact_with_an_infected_in_last_14_days:
        return True
    return False
