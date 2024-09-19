# #创建一个滑动条代码如下：
import cv2
#回调函数
def callback(pos):
    print(pos)
    print("当前用户滑动了滑动条")
cv2.namedWindow("win")
bar = cv2.createTrackbar("example" , "win", 0, 20, callback)
cv2.waitKey()


#回调函数
# def avg(x,y):
#     return (x+y)/2
#
# def f(avg,a,b):
#     return avg(a,b)
#
# ret = f(avg,1,2)
# print(ret)