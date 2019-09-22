"""华为杯全国大学生数学建模   WEKEEP团队    2019年9月23日
   该代码用于：划分后的运动学片段，绘制其中的一段速度时间曲线"""





import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

filename = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\文件23\hui_tu_3.csv"
with open(filename) as f:
    reader = csv.reader(f)
    data = next(reader)

data_ms = []
for i in data:
        try:
            h = float(i)
        except ValueError:
            pass
        else:
            k = h/(3.6)
            data_ms.append(k)



    # dates, highs, lows = [], [], []
    # for row in reader:
    #     try:
    #         date = datetime.strptime(row[0], '%Y-%m-%d')
    #         high = int(row[0])
    #     except ValueError:
    #         print(date, "missing data")
    #     else:
    #         highs.append(high)
    #         lows.append(low)
    #         dates.append(date)


"""绘图"""
fig = plt.figure(figsize=(15, 9))
plt.plot(data_ms, c='blue', linewidth=3)
# plt.plot(data, c = 'blue', linewidth = 2, alpha = 0.5)
# plt.fill_between(dates, lows, highs, facecolors = 'blue', alpha = 0.1)
plt.title('Driving Cycle Graph (File 3)', fontsize=24)

"""对x轴坐标操作"""
plt.xlabel("Time (s)", fontsize=14)
# plt.xlim(datetime(2014, 1, 1), datetime(2014, 12, 22)) #设置坐标轴上下限
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) #设置日期格式
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 30))   #设置日期间隔
# fig.autofmt_xdate()  #将x轴的日期横坐标倾斜显示，以免重叠

"""对y轴坐标操作"""
plt.ylabel("Velocity (m/s)", fontsize=14)
# plt.yticks(range(10,80,10))
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('文件3_绘图_第一段', bbox_inches = 'tight')
plt.show()  #渲染图
