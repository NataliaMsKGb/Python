# Напишите программу, которая рпинимает на вход дробь и показывает первую цифру дробной части числа

from unittest import result


number = float(input())
result = (number*10)%10
if result == 0:
    print('нет')
else:
    print(int(result))