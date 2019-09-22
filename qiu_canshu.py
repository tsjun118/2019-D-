"""华为杯全国大学生数学建模   WEKEEP团队    2019年9月23日
   该文件代码用于：求解特征参数矩阵"""

import  csv
import pandas as pd
from function_define import *


dist, v_average, v_max, shijian, daisu_shijian, jiasu_shijian, jiansu_shijian = [],[],[],[],[],[],[]
yunsu_shijian, a_max, a_min = [], [],[]
a_jia_mean, a_jian_mean = [], []

filename = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\gps_fenduan_没有空格.csv"
filepath1 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\运行距离.txt"
filepath2 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\平均速度.txt"
filepath3 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\最大速度.txt"
filepath4 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\运行时间.txt"
filepath5 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\怠速时间.txt"
filepath6 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\加速时间.txt"
filepath7 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\减速时间.txt"
filepath8 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\匀速时间.txt"
filepath9 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\最大加速度.txt"
filepath10 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\最小加速度.txt"
filepath11 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\加速度段的平均加速度.txt"
filepath12 = r"C:\Users\Administrator.SC-201808311724\Desktop\jianmo2\十二参数\减速度段的平均减速度.txt"


one_line_float = []
csv_file = open(filename)
csv_reader_lines = csv.reader(csv_file)
cout = 0
for one_line in csv_reader_lines:
    cout = cout + 1
    if (cout % 2) == 0:
        pass
    else:
        dist_row = 0
        for j in range(len(one_line)):
            try:
                h = float(one_line[j])
            except ValueError:
                pass
            else:
                one_line_float.append(h)
        # dist_row = sum(one_line_float)
        # for i in range(len(one_line_float)):
        #         dist_row += one_line_float[i]
        dist_row = sum(one_line_float)
        a = len(one_line_float)

        dist.append(dist_row)               #运行距离L
        v_average.append(dist_row/a)        #平均速度
        v_max.append(max(one_line_float))   #最大速度
        shijian.append(a)                   #运行时间
        k = daisu(one_line_float)
        daisu_shijian.append(k)             #怠速时间

        tt = jiasu(one_line_float)

        jiasu_shijian.append(tt[0])         #加速时间
        jiansu_shijian.append(tt[1])        #减速时间

        qq = a - tt[0] - tt[1]
        yunsu_shijian.append(qq)            #匀速时间

        ss = jiasu_max_min(one_line_float)
        a_max.append(ss[0])                    #最大加速度
        a_min.append(ss[1])                    #最小加速度

        a_jia_mean.append(tt[2])
        a_jian_mean.append(tt[3])           #减速度均值

        one_line_float = []


save_txt(filepath1,dist)
save_txt(filepath2,v_average)
save_txt(filepath3,v_max)
save_txt(filepath4,shijian)
save_txt(filepath5,daisu_shijian)
save_txt(filepath6,jiasu_shijian)
save_txt(filepath7,jiansu_shijian)
save_txt(filepath8,yunsu_shijian)
save_txt(filepath9,a_max)
save_txt(filepath10,a_min)
save_txt(filepath11,a_jia_mean)
save_txt(filepath12,a_jian_mean)



print("成功")
# print(len(dist))
# print(dist)





# with open(filename) as f:
#     reader = csv.reader(f)
#     rows = [row for row in reader]
#
# print(rows)






# for row in reader:
#     row_data = next(reader)
#     print(len(row_data))
#     c
# dist, v_average, v_max, shijian, daisu_shijian, jiasu_shijian, jiansu_shijian = [],[],[],[],[],[],[]
#
#
# print(data)