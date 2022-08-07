filename = 'pi_digits.txt'

'''
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

birthday = input('输入你的生日：')
if birthday in pi_string:
    print(1)
else:
    print(0)
'''

'''
#try...except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print('除数不能为0.')
'''


'''try..except..else代码块
first_number = input('被除数：')
last_number = input('除数：')
try:
    answer = int(first_number)/int(last_number)
except ZeroDivisionError:
    print('除数不能为0.')
else:
    print(answer)
'''
'''
title = 'an hui university'
#根据字符串创建一个单词列表
words = title.split()
print(len(words))
'''

