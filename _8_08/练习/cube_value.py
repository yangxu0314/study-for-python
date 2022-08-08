import matplotlib.pyplot as plt

#显示前五个数的立方值

value_x = [1, 2, 3, 4, 5]
value_y = [1, 8, 27, 64, 125]

#显示前五千的数的立方值
'''
value_x = list(range(1,5001))
value_y = [x**3 for x in value_x]
'''
#立方值折线图
plt.plot(value_x, value_y, linewidth=5)
#plt.scatter(value_x, value_y, c=value_y, edgecolors='none', cmap=plt.cm.Reds, s=10)
'''设置标题和坐标抽标签'''
plt.title('cube value', fontsize=25)
plt.xlabel('value', fontsize=15)
plt.ylabel('cube of value', fontsize=15)
'''设置刻度范围'''
#plt.axis([0, 5100, 0, 1.51e11])
'''设置刻度值字体'''
plt.tick_params(axis='both', labelsize=15)
#展示
#plt.show()
#生成文件
plt.savefig('cube_1_5.png')
