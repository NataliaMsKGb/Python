# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.


def show(array: [list]):
    print('|', end=' ')
print(*range(len(array)), sep=' | ', end=' | \n')
print('—————————————')
for i, row in enumerate(array):
    print('|', end=' ')
print(*row, sep=' | ', end=f' | {i}\n')
print('—————————————')
