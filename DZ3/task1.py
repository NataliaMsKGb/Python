# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from file_def import get_list

# input_list = get_list()
# print(f'Сумма элементов списка, стоящих на нечетных позициях: '
# f'{sum(el for i, el in enumerate(input_list) if i % 2)}')

import random
s = []
for i in range(int(input('Размер списка: '))):
    s.append(random.randint(-10,10))

result = s[1::2]
print(s)
print(f'Элементы на нечетных позициях - {result}, сумма  элементов = {sum(result)}')

