#-*-coding:utf-8 -*-
import math     #   导入数学库,用π.
#   定义了3种形状的图形,三角,矩形,圆形

class Triangle(object):
    def __init__(self,x,y,z):
        '''
        x,y,z分别为三角形的三个边的长度,一定要满足关系 z < x+y & x < y+z & y < x+z .
        '''
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        '''
        计算周长,公式 sum = x+y+z
        '''
        p = self.x + self.y + self.z
        return p    #   返回周长
    
    def area(self):
        '''
        计算面积,公式:海伦公式
        '''
        p = float(self.perimeter()) / 2     #   对周长进行一次类型转换,禁用底板除
        s = (p*(p-self.x)*(p-self.y)*(p-self.z))**0.5
        return s
    
    def display(self):
        print("三角形的边长分别为: x = {0} , y = {1} , z = {2} .".format(self.x,self.y,self.z))
        print("三角形的周长为: {} .".format(self.perimeter()))
        print("三角形的面积为: %f ."%(self.area()))

class Circle(object):
    def __init__(self,r):
        '''
        定义一个圆形,半径为r
        '''
        self.r = r
        
    def perimeter(self):
        '''
        计算周长,公式:p = 2πr
        '''
        p = 2 * math.pi * self.r
        return p
    
    def area(self):
        '''
        计算面积,公式:s = πr^2
        '''
        s = math.pi * self.r * self.r
        return s
    
    def display(self):
        print("圆形半径为: %d ."%(self.r))
        print("圆形的周长为: %d ."%(self.perimeter()))
        print("圆形的面积为: %d ."%(self.area()))
        
class Retangle(object):
    def __init__(self,l,h):
        '''
        初始化一个矩形,l为长,h为高
        '''
        self.h = h
        self.l = l
        
    def perimeter(self):
        '''
        计算矩形周长 : 2(l + h)
        '''
        p = 2 * (self.h + self.l)
        return p
    
    def area(self):
        '''
        计算矩形面积 : h*l
        '''
        s = self.h * self.l
        return s
    
    def display(self):
        print("矩形的长高分别为: l = {0} , h = {1} .".format(self.l,self.h))
        print("矩形的周长为: %d ."%(self.perimeter()))
        print("矩形的面积为 %d ."%(self.area()))
        
    
        