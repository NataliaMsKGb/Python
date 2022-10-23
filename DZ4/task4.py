# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0




import random

k = 3
random_number_list = [random.randint(0, 10)for i in range(k+1)]
print(random_number_list)
uravnenie = []
# y = 3*x**3 + 10*x**2 + 15*x + 85
# y = 3*x**3 + 15*x + 85
for i in range(len(random_number_list) - 1):
    if random_number_list[i] != 0:
        if k-i == 1:
            uravnenie.append(f"{random_number_list[i]}*x")
        else:
            uravnenie.append(f"{random_number_list[i]}*x**{k - i}")
uravnenie.append(str(random_number_list[-1]))

text = (' + '.join(uravnenie))
with open('info.txt', 'a') as file:
    file.write(text)
    # file.write('\n')