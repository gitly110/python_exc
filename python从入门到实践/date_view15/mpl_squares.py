import matplotlib.pyplot as plt


# 设置图表标题，并给坐标轴加上标签
def lable_draw():
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Square of Value', fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)


x_values = list(range(1001))
y_values = [x ** 2 for x in x_values]
# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

lable_draw()
'''
递参数c ，并将其设置为一个元组，其中包含三个0~1之间的小数值，
它们分别表示红色、绿色和蓝色分量。值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
'''
plt.plot(x_values, y_values, c=(0, 0, 0.5), linewidth=3)  # 绘制线条的粗细
plt.show()

lable_draw()
# 参数c ，并将其设置为要使用的颜色的名称
plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)  # 绘制点
plt.show()
