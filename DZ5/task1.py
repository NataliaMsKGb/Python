# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import re

s = "автобус аэробус машина зимбабве самозабвенный главрыба Напишите программу, удаляющую из текста все слова, содержащие"
#words = s.split()
words = re.split('\W+', s)

ex = ["а", "б", "в"]

for i in range(len(words)):
    if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
        words[i] = None
# print (' '.join(words))
words = [txt for txt in words if txt]
print(*words)




# s = 'напишите программу, удаляющую из текста все слова, содержащие "абв" автобус'.split()
# print(s)
# result = filter(lambda x: 'а' not in x or 'б' not in x or 'в' not in x, s)
# print(*result)

# print(' '.join(filter(lambda x: not any(True if char in x else False for char in 'абв'), text.split())))



# print(*filter(lambda x: not set(x) >= (set('абв')), text.split()), sep=' ') # issuperset



# print(*filter(lambda x: set(x).isdisjoint(set('абв')), text.split()), sep=' ')
