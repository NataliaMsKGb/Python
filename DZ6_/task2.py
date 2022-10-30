# 2 – Дана последовательность чисел. Получить список уникальных элементов заданной
# последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]



datalist = [1, 2, 3, 5, 1, 5, 3, 10]

# print(list(set([1, 2, 3, 5, 1, 5, 3, 10])))

datauniq = [i for i in datalist if datalist.count(i) == 1]
print(datauniq)

datadouble = list(set([i for i in datalist if datalist.count(i) != 1]))
print(datadouble)

data_del_double = list(set(datalist))
print(data_del_double)
