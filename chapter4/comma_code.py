spam = ['apples', 'bananas', 'tofu', 'cats']

# def comma_code(list):
#     for i in range(len(list)):
#         if i == len(list) - 1:
#             print('and ' + list[i])
#         else:
#             print(list[i] + ', ', end='')

def comma_code(list):
  print(', '.join(list[:-1]) +', and '+ list[-1])

comma_code(spam)