from numbers import *


def person_data(i):

    list_name_m = 'Иван Виктор Андрей Игорь Роман Александр Антон Алексей Юрий Евгений'.split()
    list_surname = 'Иванов Петров Сидоров Андреев Антонов Кузнецов Александров Михайлов'.split()
    list_name_w = 'Ольга Татьяна Елена Анна Ирина Яна Алина Мария Алена Екатерина'.split()
    list_job = 'Завод Больница Школа Полиция Офис Магазин Транспорт Связь'.split()

    gender = random.randint(0, 1)
    if gender == 0:
        return {
                "id":f'{i}' ,
                "Имя": f"{random.choice(list_name_w)}",
                "Фамилия": f"{random.choice(list_surname)}а",
                "Возраст": f"{random.randint(18,60)}",
                "место работы":f"{random.choice(list_job)}",
                "номер телефона": f"{create_number()}"}
    if gender == 1:
            return {
                "id":f'{i}' ,
                "Имя": f"{random.choice(list_name_m)}",
                "Фамилия": f"{random.choice(list_surname)}",
                "Возраст": f"{random.randint(18,65)}",
                "место работы":f"{random.choice(list_job)}",
                "номер телефона": f"{create_number()}"}

