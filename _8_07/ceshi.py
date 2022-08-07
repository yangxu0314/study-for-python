'''
from _8_07 import get_formatted_name
print("任何时候输入0结束")
while True:
    first = input("输入你的姓: ")
    if first == 'e':
        break
    last = input("输入你的名: ")
    if last == 'e':
        break
    full_name = get_formatted_name(first, last)
    print("完整的名字是:" + full_name)
'''


import unittest
from _8_07 import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试day2'''

    def test_first_last_name(self):
        '''能否正确运行含有名姓的名字'''
        full_name = get_formatted_name('yang', 'xu')
        self.assertEqual(full_name, 'Yang Xu')
        #self.assertEqual(full_name, 'yang xu')

    def test_first_last_middle_name(self):
        '''能否正确运行含有中间名的名字'''
        full_name = get_formatted_name('yang', 'xu', "shuai")
        self.assertEqual(full_name, 'Yang Shuai Xu')

unittest.main()#让python运行文件中的测试