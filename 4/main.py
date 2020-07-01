#-*- coding:utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt 
 
#   将气温写入一个pandas数据帧中
datas = pd.DataFrame([[2,5,12,20,26,30,31,30,26,19,10,3],[-9,-6,0,8,14,19,22,21,15,8,0,-6],[3,6,9,22,36,74,179,177,53,23,8,2]]\
    ,index=['Daily Maximum Temperature(℃)','Daily Minimum Temperature(℃)','Average Precipitation(mm)']\
    ,columns=['January','February','March','April','May','June','July','August','September','October','November','December'])

#   matplotlib默认不支持中文我就用了英文的索引标记
#   第一题,画出全年每个月的日均最高气温的折线图,红色
def draw_1():
    x = datas.columns
    y = datas.loc['Daily Maximum Temperature(℃)']
    plt.figure(figsize = (20,8),dpi=100)
    plt.title("Beijing's Daily Maximum Temperature(line chart)")
    plt.xlabel("Month")
    plt.ylabel("Daily Maximum Temperature(℃)")
    plt.plot(x,y,'r',linewidth=5.0)
    plt.savefig("./1.png")  # 保存
    plt.show()  # 显示
    
#   第二题,画出最低气温
def draw_2():
    x = datas.columns
    y = datas.loc['Daily Minimum Temperature(℃)']
    plt.figure(figsize = (20,8),dpi=100)
    plt.title("Beijing's Daily Minimum Temperature(line chart)")
    plt.xlabel("Month")
    plt.ylabel("Daily Minimum Temperature(℃)")
    plt.plot(x,y,'b',linewidth=5.0)
    plt.savefig("./2.png")  # 保存
    plt.show()  # 显示
    
#   第三题,合并2个图
def draw_3():
    x = datas.columns
    y1 = datas.loc['Daily Minimum Temperature(℃)']
    y2 = datas.loc['Daily Maximum Temperature(℃)']

    plt.figure(figsize = (20,8),dpi=100)
    plt.title("Beijing's Daily Minimum Temperature(line chart)")
    plt.xlabel("Month")
    plt.ylabel("Daily Minimum Temperature(℃)")
    plt.plot(x,y1,'b',y2,'r',linewidth=5.0)
    ###############################                                         # 网上抄的改了改.
    ax = plt.gca()#获取当前坐标的位置
    ax.xaxis.set_ticks_position('bottom') # 设置bottom为x轴
    ax.yaxis.set_ticks_position('left') # 设置left为x轴
    ax.spines['right'].set_color('none') 
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data',0))#这个位置的括号要注意
    #ax.spines['left'].set_position(('data',0))
    ###############################
    plt.savefig("./3.png")  # 保存
    plt.show()  # 显示
#   第四题,全年平均降水柱状图
def draw_4():
    x = datas.columns
    y = datas.loc['Average Precipitation(mm)']
    plt.figure(figsize = (20,8),dpi=100)
    plt.title("Beijing's Average Precipitation(line chart)")
    plt.xlabel("Month")
    plt.ylabel("Average Precipitation(mm)")
    plt.bar(x,y,color ='g',align='center')
    plt.savefig("./4.png")  # 保存
    plt.show()  # 显示
if __name__ == "__main__":
    draw_1()
    draw_2()
    draw_3()
    draw_4()