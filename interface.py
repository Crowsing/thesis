import data
from calculating.recommendation import calculating_a_recommendation


def interface():
    sex = str
    age = int
    additional_diseases = []
    main_symptoms = []
    additional_symptoms = []
    suggestive_questions = []
    body_temperature = ''
    contact_with_an_infected_in_last_14_days = ''

    print("Вкажіть Вашу стать: ")
    print("1) Жінка")
    print("2) Чоловік")
    user_chose = int(input())
    if user_chose == 1:
        sex = 'woman'
    else:
        sex = 'man'

    age = int(input("Введіть Ваш вік: "))
    while age >= 120 or age <= 0:
        age = int(input("Введіть Ваш вік: "))

    print("Відзначте всі положення, які відносяться до Вас:")
    while True:
        diagnosis_id = int(input("1) В даний час є злоякісна пухлина\n"
                                 "2) Ослаблений імунітет\n"
                                 "3) Ожиріння\n"
                                 "4) Цукровий діабет\n"
                                 "5) Сердечно - судинні захворювання\n"
                                 "6) Є хронічне захворювання легенів\n"
                                 "7) Хронічне захворювання печінки в анамнезі\n"
                                 "8) Ниркова недостатність в анамнезі\n"
                                 "0) Далі\n"))

        if diagnosis_id == 0:
            break

        diagnosis = list(data.additional_diseases.keys())[diagnosis_id - 1]
        if diagnosis not in additional_diseases:
            additional_diseases.append(diagnosis)
        else:
            print('Ви вже додали це захворювання')

    print("Чи є у Вас якісь із наступних симптомів? Виберіть тільки симптоми, які з\'явилися зараз і не пов\'язані з "
          "наявними у Вас хронічним захворюванням.")
    for key in data.main_symptoms.keys():
        print(key)
        user_chose = int(input('1) Так\n2) Ні\n'))
        if user_chose == 1:
            main_symptoms.append(key)

    if 'Висока температура тіла' in main_symptoms:
        print('Яка у Вас температура тіла?')
        for index, temp in enumerate(data.body_temperature.keys()):
            print(f'{index + 1}) {temp}')
        user_chose = int(input())
        body_temperature = list(data.body_temperature.keys())[user_chose - 1]

    if main_symptoms:
        for suggestive_question in data.suggestive_questions.keys():
            print(suggestive_question)
            user_chose = int(input('1) Так\n2) Ні\n'))
            if user_chose == 1:
                suggestive_questions.append(suggestive_question)

    print("Чи є у Вас якісь із наступних симптомів?")
    while True:
        symptom_id = int(input("1) Патологічна стомлюваність\n"
                               "2) Біль у м\'язах\n"
                               "3) Головний біль\n"
                               "4) Діарея\n"
                               "5) Нудота\n"
                               "6) Біль в горлі\n"
                               "7) Нежить\n"
                               "8) Відсутність апетиту\n"
                               "0) Далі\n"))

        if symptom_id == 0:
            break

        symptom = list(data.additional_symptoms.keys())[symptom_id - 1]
        if symptom not in additional_symptoms:
            additional_symptoms.append(symptom)
        else:
            print('Ви вже додали це захворювання')

    print('Контактували Ви в останні 14 днів з людиною з підозрою на інфекцію COVID-19?')
    for index, item in enumerate(data.contact_with_an_infected_in_last_14_days):
        print(f'{index + 1}) {item}')
    user_chose = int(input())
    contact_with_an_infected_in_last_14_days = data.contact_with_an_infected_in_last_14_days[user_chose - 1]

    print(calculating_a_recommendation(
        sex,
        age,
        additional_diseases,
        main_symptoms,
        additional_symptoms,
        suggestive_questions,
        body_temperature,
        contact_with_an_infected_in_last_14_days
    ))
