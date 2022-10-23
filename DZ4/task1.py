# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)


import math

p =  math.pi
# print(p)

d = 0.001
count = 0           
while d < 1:
    count += 1
    d*=10

print(round(p, count))

