# Напишите программу, которая определяет позицию второго вхождения строки в список либо сообщает, что ее нет
lst  =['1', 'qwe', 'oko2', 'qwe', '54']
N = input('Введите строку:   ')

counter = 0
target_counter = 2
for i in range(len(lst)):
    if N == lst[i]:
        counter +=1
        if counter == target_counter:
            print(f'Строка {N} найдена в списке. Ее {counter} нахождение под индексом  {i}')
            break
else:
    print('нет второго вхождения')
