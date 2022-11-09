# Напишите программу, которая определит, присутствует ли в данном списке строк некое число
# lst  =['1', 'nkj5', 'oko2', '10111111111111', '54']
# N = input('Введите число:   ')
# for item in lst:
#     if N in item:
#         print('cool')
#         break
# else:
#     print('no')



lst  =['1', 'nkj5', 'oko2', '10111111111111', '54']
num = 8
for i in lst:
    if str(num) in i:
        print('yes')
        break
else:
    print('no')
