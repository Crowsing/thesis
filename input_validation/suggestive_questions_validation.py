import data


def suggestive_questions_validation(suggestive_questions: list):
    """
    Перевірка корректності даних про захворювання пацієнта
    :param suggestive_questions: list
    :return: boolean
    """
    if not suggestive_questions:
        return True

    for suggestive_question in suggestive_questions:
        if suggestive_question not in data.suggestive_questions:
            return False

    return True
