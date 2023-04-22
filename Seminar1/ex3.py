# Напищите программу, которая принимает на вход число и проверяет, кратно ли оно 5, 10 или 15, но не 30

from tkinter import N
from xmlrpc.client import boolean


print ('input N')
num = int(input())
# if ((num % 5 ==0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0:
#     print('кратно')
# else: print('не кратно')
print(bool(((num % 5 ==0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0))
