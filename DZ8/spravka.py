import json
import generate_person

data = {}

for i in range(1,6):
    data[str(i)] = generate_person.person_data()


def set_info():
    with open("classmates.json", mode="w", encoding='utf-8') as w_file:
        names = ["id", "Имя", "Фамилия", "Дата рождения", "место работы", "номер телефона"]
        json.dump(data, w_file, indent=4)


def get_info():
    with open("classmates.json", mode='r', encoding='utf-8') as r_file:
        file_reader = json.load(r_file)
        for i, n in file_reader.items():
            print(f'\n{i}')
            for k,value in n.items():
                print(f'\t{k}:{value}')


while True:
    print('\nПросмотр данных - 1'
          '\nИзменение данных - 2'
          '\nДобавление данных - 3')
    action = input("Введите номер команды: ")
    if action == '1':
        get_info()
    elif action == '2':
        answer = input("Знаете ли вы id (да/нет): ").lower()
        if answer == "да":
            id = input("Введите id:")
            if id in data:
                print(data[id])
                answer_2 = input("Что хотите изменить: имя/фамилия/дата рождения/телефон/группа: ").lower()
                if answer_2 == 'имя':
                    new_name = input('Введите новое имя: ')
                    data[id]['Имя'] = new_name
                elif answer_2 == 'фамилия':
                    new_surname = input('Введите новую фамилию: ')
                    data[id]['Фамилия'] = new_surname
                elif answer_2 == 'дата рождения':
                    new_born = input('Введите новую дату рождения: ')
                    data[id]['Дата рождения'] = new_born
                elif answer_2 == 'группа':
                    new_group = input('Введите новую группу: ')
                    data[id]['Группа'] = new_group
                elif answer_2 == 'телефон':
                    new_number = input('Введите новый телефон: ')
                    data[id]['Телефон'] = new_number
                else: print("Некорректный ввод данных")
            else: print("id не найден")
        else:
            print('Тогда ищите в списке')
            get_info()
    elif action == '3':
        result = generate_person.set_new_person()
        data [len(data)+1] = result
        set_info()
    else:print("Введена неверная команда")

