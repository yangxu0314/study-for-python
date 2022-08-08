import matplotlib.pyplot as plt

#绘制单个点
#plt.scatter(2, 4, s=200)

#绘制一系列散点
'''
value_x = [1, 2, 3, 4, 5]
value_y = [1, 4, 9, 16, 25]
plt.scatter(value_x, value_y, s=100)
'''
#绘制1000个点
value_x = list(range(1, 1001))
value_y = [x**2 for x in value_x]
#edgecolor是散点的轮廓,参数c能够设置散点颜色
plt.scatter(value_x, value_y, edgecolors='none', c=value_y, cmap=plt.cm.Reds , s=40)
#设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])


#设置图表标题，并给坐标轴加上标签
plt.title('square number', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
#展示
#plt.show()
#将图标保存到文件
plt.savefig('square_plot1.png')