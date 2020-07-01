#-*- coding:utf-8 -*-
import pandas as pd

#   第一题,使用DataFrame
def loading_csv_data(src):
    '''
    读取src地址的csv格式文件,并且返回DataFrame类型的变量
    '''
    res = pd.DataFrame(pd.read_csv(src))
    return res

#   第二题,输出数据行数,属性数
def size_of_data(df):
    print("数据表共有 %d 行数据."%len(df.index))
    print("数据表共有 %d 项属性."%len(df.columns))

#   第三题,输出所有队伍的红,黄牌数量
def total_cards(df):
    tmp = zip(df['Team'],df['Yellow Cards'],df['Red Cards'])
    for i in tmp:
        print("队伍[{}]:黄牌总数为{}张,红牌总数为{}张.".format(i[0],i[1],i[2]))

#   第四题,全部比赛一个进了多少个球?平均每个球队进多少球.
def goals(df):
    print("全部比赛一共进了{}个球,平均每个球队进了{}个球.".format(df['Goals'].sum(),df['Goals'].mean()))

#   第五题,输出传球准确率最高的是哪个球队
def precision(df):
    team_name = list(df['Team'])
    precision_ratio = list(df['Passing Accuracy'])
    tmp = dict()
    #   为 球队:传球准确率 创建一个字典
    for i in range(len(team_name)):
        tmp.update({team_name[i]:precision_ratio[i]})
    #   将字典排序,并且输出前三个
    tmp = sorted(tmp.items(),key=lambda x:x[1],reverse=True)
    for i in range(3):
        print("第{}名:[{}]队,传球精确率{}.".format(i,tmp[i][0],tmp[i][1]))
    
#   全部显示输出
def display_all():
    '''
    改变pandas的全局变量
    '''
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)


if __name__ == "__main__":
    df = loading_csv_data("./file1.csv")
    #   display_all()
    print("*"*50)
    print(df)
    print("*"*50)
    size_of_data(df)
    print("*"*50)
    total_cards(df)
    print("*"*50)
    goals(df)
    print("*"*50)
    precision(df)