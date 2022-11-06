import csv
from create_data import *


with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    names = ["id", "Имя", "Фамилия", "Возраст", "место работы", "номер телефона"]
    file_writer = csv.DictWriter(w_file, delimiter = ",",
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    for i in range(500):
        file_writer.writerow(person_data(i))

with open("classmates.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ',')
    for i in file_reader:
        print(" ".join((i)))


