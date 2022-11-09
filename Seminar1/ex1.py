# Напишите программу, которая принимает на вход число N и выводит от -N до N.

from os import sep
from tkinter import N


number = int(input())
# for value in range (-number, number+1):
#     print(value, end = ', ')

print(*range (-number, number+1), sep = ', ')
