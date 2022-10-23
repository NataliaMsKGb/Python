# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

# A = int(input('Введите число А:  '))
# B = int(input('Введите число B:  '))
# C = int(input('Введите число C:  '))


# D = B * B - 4 * A * C  
# x1 = (-B + D ** (1/2)) / (2*A)
# x2 = (-B - D ** (1/2)) / (2*A)

# print(f'Корень квадратного уравнения {A}x^2 + {B}x + {C} = 0: {x1}, {x2}')


import sympy

x  = sympy.Simbol("x")

print(sympy.solveset(1*x**2*x+3,x))



# print("Ax² + Bx + C = 0")
# a = float(input('Введите А: '))
# b = float(input('Введите B: '))
# c = float(input('Введите C: '))

# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)

# if discr > 0:
# x1 = (-b + math.sqrt(discr)) / (2 * a)
# x2 = (-b - math.sqrt(discr)) / (2 * a)
# print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
# x = -b / (2 * a)
# print("x = %.2f" % x)
# else:
# print("Корней нет")
