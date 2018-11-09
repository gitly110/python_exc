import csv
from datetime import datetime
from matplotlib import pyplot as plt


# 从文件获取最高、最低气温
def read_csv(filename):
    # filename = 'sitka_weather_2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        hearder_row = next(reader)
        # # 查看文件头每个元素的索引及其值
        # for index, column_header in enumerate(hearder_row):
        #     print(index,column_header)
        dates, highs, lows = [], [], []
        for row in reader:  # 遍历文件中余下的各行
            try:
                # 每行索引为0的是日期，转为日期格式存入列表
                date = datetime.strptime(row[0], "%Y-%m-%d")
                # 每行索引为1的是最高温度，转为数字存入列表
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(date, 'missing data')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows


dates1, highs1, lows1 = read_csv('sitka_weather_2014.csv')
dates2, highs2, lows2 = read_csv('death_valley_2014.csv')

# 根据数据绘制图`
fig = plt.figure(dpi=128, figsize=(10, 6))
# alpha 指定颜色的透明度。Alpha 值为0表示完全透明，1（默认设置）表示完全不透明
# sitka_weather_2014
plt.plot(dates1, highs1, c='red', alpha=0.5)
plt.plot(dates1, lows1, c='blue', alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)
# death_valley_2014
plt.plot(dates2, highs2, c='yellow', alpha=0.5)
plt.plot(dates2, lows2, c='green', alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor='green', alpha=0.1)
#
# # 设置y轴范围
# plt.ylim(0, 120)
# 设置图形格式
plt.title('Daily high and low temperature 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 调用了fig.autofmt_xdate() 来绘制斜的日期标签
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
