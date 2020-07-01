#-*- coding:utf-8 -*-
import shape

if __name__ == "__main__":
    tri = shape.Triangle(1,1,1)     #   1,1,1的全等三角形
    re = shape.Retangle(4,2)        #   4,2的矩形
    cri = shape.Circle(3)           #   半径为3的圆形
    
    print("*"*25)
    tri.display()
    print("*"*25)
    re.display()
    print("*"*25)
    cri.display()
    print("*"*25)