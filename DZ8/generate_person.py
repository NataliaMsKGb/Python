
import random


def create_number():
    number = '+7'
    for i in range(10):
        number += str(random.randint(0, 9))
    return number


def person_data():

    list_name_m = 'Иван Виктор Андрей Игорь Роман Александр Антон Алексей Юрий Евгений'.split()
    list_surname = 'Иванов Петров Сидоров Андреев Антонов Кузнецов Александров Михайлов'.split()
    list_name_w = 'Ольга Татьяна Елена Анна Ирина Яна Алина Мария Алена Екатерина'.split()
    list_faculty = 'А Б В Г'.split()

    gender = random.randint(0, 1)
    date_born = f'{random.randint(1,28)}.{random.randint(1,12)}.{random.randint(1998,2004)}'
    name = f"{random.choice(list_name_w)}"
    surname = f"{random.choice(list_surname)}а"
    group = f"{random.choice(list_faculty)}"

    if gender == 0:
        return {
                "Имя": f"{name}",
                "Фамилия": f"{surname}а",
                "Дата рождения": f"{date_born}",
                "Группа":f"{group}",
                "Телефон": f"{create_number()}"}
    if gender == 1:
            return {
                  "Имя": f"{name}",
                "Фамилия": f"{surname}",
                "Дата рождения": f"{date_born}",
                "Группа":f"{group}",
                "Телефон": f"{create_number()}"}

def set_new_person():
    date_born = input("Введите дату рождения дд.мм.гггг")
    name = input("Введите имя")
    surname = input("Введите дату фамилию")
    group = input("Введите группу")
    number = input("Введите телефон")


    return {
            "Имя": f"{name}",
            "Фамилия": f"{surname}а",
            "Дата рождения": f"{date_born}",
            "Группа":f"{group}",
            "Телефон": f"{number}"}
