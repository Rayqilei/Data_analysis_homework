#-*- coding:utf-8 -*-
import numpy as np
import sys
'''
#  定义numpy数组的数据类型,我决定使用二维数组来进行运算,下面是一个数据项代表的含义
# ANALYSE = np.dtype([('math','int8'),('chinese','int8'),\
#     ('physics','int8'),('chemistry','int8'),('foreign','int8'),('politics','int8')])
'''

###############################################################################################################
# 下面是第一个问题,将成绩单用Numpy的二位数组进行表示
ANALYSE = np.dtype(float)

#   定义Numpy数组,我们将它定义为全局变量,根据PY的编程习惯,我们将全局变量定义为全大写的变量名字,方便我们进行区分,增加代码的可读性
STUDENT_T1 = np.array([[90,80,95,93,85,75],[91,92,90,88,86,87],[83,96,80,85,93,90]],dtype=ANALYSE)
###############################################################################################################

#   下面的函数是第二问的问题,计算三个学生的平均成绩
def averaging(tmp,out = sys.stdout):
    '''
    输出三个学生的各科平均分,输出物理课的平均成绩,并且保留2位有效数字
    '''
    print("*"*20,file=out)
    print("学生1的平均分为: %.2f"%np.average(tmp[0]),file=out)
    print("学生2的平均分为: %.2f"%np.average(tmp[1]),file=out)
    print("学生3的平均分为: %.2f"%np.average(tmp[2]),file=out)
    print("物理课的平均成绩为: %.2f"%np.average(tmp[...,2]),file=out)
 ###############################################################################################################
 
#   下面的函数是第三个问题,计算加权平均
def weighted_averaging(tmp,out = sys.stdout):
    weight = np.array([2,2,1,1,2,1])
    print("*"*20,file=out)
    print("学生1的加权平均分为: %.2f"%np.average(tmp[0],weights=weight),file=out)
    print("学生2的加权平均分为: %.2f"%np.average(tmp[1],weights=weight),file=out)
    print("学生3的加权平均分为: %.2f"%np.average(tmp[2],weights=weight),file=out)
 ###############################################################################################################
 
 #  下面是第四题,找出成绩最均衡和最不均衡的学生
def standard_deviating(tmp,out = sys.stdout):
    '''
    处理均衡程度,我们需要使用方差或者标准差进行统计,此处我使用了标准差
    '''
    print("*"*20,file=out)
    res = list()
    p = 0
    q = 0 
    for i in range(tmp.shape[0]):
        res.append(np.std(tmp[i]))
    for i in range(len(res)):
        if res[i] > p:
            p = res[i]
            q = i
    print("学习成绩最不均衡的学生是: 学生 %d [%f]"%(q+1,p),file=out)
    for i in range(len(res)):
        if res[i] < p:
            p = res[i]
            q = i
    print("学习成绩最均衡的学生是: 学生 %d [%f]"%(q+1,p),file=out)
###############################################################################################################

#   第五题,输出盖成绩单到score.txt,使用了print中的file参数,对我们运行终端输出进行了重定向,
#   上面的函数中我们定义默认的输出流是sys.stdout,在这里为了输出结果,我们将流定向了建立的score.txt文件
def output_file(tmp):
    f = open("./score.txt","w")
    f.write("      数学  语文  物理  化学  外语  政治\n")
    for i in range(tmp.shape[0]):
        f.write("学生"+str(i)+" : ")
        for j in tmp[i]:
            f.write(str(int(j))+' , ')
        f.write('\n')
        
    averaging(STUDENT_T1,f)   
    weighted_averaging(STUDENT_T1,f)
    standard_deviating(STUDENT_T1,f)
    f.close()

if __name__ == "__main__":
    averaging(STUDENT_T1)   
    weighted_averaging(STUDENT_T1)
    standard_deviating(STUDENT_T1)
    output_file(STUDENT_T1)