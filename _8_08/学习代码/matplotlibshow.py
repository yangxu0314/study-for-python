import matplotlib.pyplot as plt#matplotlib是数据绘图库   pyplot是它的一个模块

in_put = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
#plt.plot(squares, linewidth=5)
plt.plot(in_put, squares, linewidth=5)

plt.title('Square Number', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()