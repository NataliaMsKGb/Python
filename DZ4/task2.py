# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите целое натуральное число:   '))
# 128 = 2*2*2*2*2*2*2 
# 63 = 3*3*7
# 52 = 2*2*13
lst  = [] 
while True:
    prime = 0
    for i in range (2,10):
        if number % i == 0:
            prime = i
            number //= i
            break
        else: 

            prime = number
            number //= number
            break
    lst.append(prime)
    if number == 1: break
    

print(lst)

