"""华为杯全国大学生数学建模   WEKEEP团队    2019年9月23日
   该文件代码用于：qiu_canshu.py文件的函数定义"""



"""保存列表数据到txt文件"""
import  numpy as np

def save_txt(filepath,data):
    with open(filepath, "a+") as f:
        for shuju in data:
                shuju_str = str(shuju)
                f.write(shuju_str)
                f.write(",")
        f.write("\r\n")

def daisu(data):
    count = 0
    for i in range(len(data)):
        if data[i] == 0:
            count = count + 1
    return count






def jiasu(data):       #加减速计时
    count_jia = 0
    count_jian = 0
    jiasudu_list = []     #存储加速度值
    jiansudu_list = []
    d = []
    for i in range(1,len(data)):
        a = data[i-1]/(3.6)
        b = data[i]/(3.6)
        c = b - a
        if c > 0.1:
            count_jia = count_jia + 1
            jiasudu_list.append(c)
        if c < -0.15:
            count_jian = count_jian + 1
            jiansudu_list.append(c)
    jiasu_average = np.mean(jiasudu_list)
    jiansu_average = np.mean(jiansudu_list)
    d.append(count_jia)
    d.append(count_jian)
    d.append(jiasu_average)     #加速度均值
    d.append(jiansu_average)    #减速度均值
    return d



def jiasu_max_min(data):      #最大最小  加速度
    jiasudu = []
    jiasudu_max_min = []
    for i in range(1, len(data)):
        a = data[i - 1] / (3.6)
        b = data[i] / (3.6)
        c = b - a
        jiasudu.append(c)
    max_1 = max(jiasudu)
    min_1 = min(jiasudu)
    jiasudu_max_min.append(max_1)
    jiasudu_max_min.append(min_1)
    return  jiasudu_max_min
