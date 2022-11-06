# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Введите число '))

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
    for i in range(1, n+1):
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))

# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
# res = 1
# for i in range(1, n+1):

#     res = res + res
#     print(res, end= ', ')



# F n = F n − 1 + F n − 2 .
# for i in range(1, n+1):