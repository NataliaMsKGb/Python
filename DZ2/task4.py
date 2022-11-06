
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.



# position =  'file.txt'
# data = open(position, 'r')
# for line in data:
#     print(line)
# data.close()


# N = int(input('Введите число: '))
# for i in range(-N, N):
#     result = i
#     print(result)


from random import randint

position = 'file.txt'
positions = []
data = open(position, 'r')
for line in data:
    positions.append(int(line))
data.close()

N = int(input('Input count: '))
# multiply = 1
# # Если количество N и элементы рандомно
# for i in range(N):
#     number=randint(-N, N)
#     print(number)
#     if i in positions:
#         multiply *= number
        
# print('Произведение рандомных чисел:', multiply)

# Если эллементы от -N до N
multiply = 1 # Обнуление для второго варианта
for i in range(-N, N + 1):
    if i in positions:
        multiply *= i
        
print('Произведение чисел от',-N, "до", str(N)+":", multiply)