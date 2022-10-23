#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
#  6782 -> 23
#  0,56 -> 11

number = float(input('Введите число:  '))
while int(number) != number:
    number *= 10
    
result = 0
while number:
    result += number % 10
    number //= 10
print(int(result))

