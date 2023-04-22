# def zip_data(text):
#     zip_a = ""
#     pred_sym = text[0]

#     count = 1

#     for i in range(1, len(text)):
#         if text[i] == pred_sym:
#             count +=1
#         else: 
#             zip_a += str(count) + pred_sym
#             pred_sym = text[i]
#             count = 1
#     zip_a += str(count) + pred_sym
#     print(zip_a)

# # zip_data(test)


# def unzip_data(text):
#     count = ""
#     new_text = ""
#     for i in text:
#         if i.isdigit():
#             count += i
#         else:
#             new_text += i * int(count)
#             count = ""     
#     print(new_text)