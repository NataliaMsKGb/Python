#  2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  Пример:
#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите целое число:  '))
res = 1
for i in range(1, n+1):
    res *= i
    print(res, end= ', ')





# def fib(N):
#     if N == 1:
#         return N
#     return N * fib(N - 1)

# N = int(input('N:  '))
# lst = []
# for i in range(1, N + 1):
#     lst.append(fib(i))
#     print(lst)
