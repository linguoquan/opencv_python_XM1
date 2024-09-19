#方法1：同时获取坐标(190,168)上的RGB像素值，代码如下：
import cv2
logo = cv2.imread('./img.png')
# 打印logo中坐标(190,168)位置的像素
print(logo[80,80])



# #方法2：分别获取坐标(190,168)上像素的B通道、G通道、R通道的值，代码如下：
# import cv2
# logo = cv2.imread('./img.png')
# blue  =  logo[80, 80, 0]
# green =  logo[80, 80, 1]
# red   =  logo[80, 80, 2]
# print(blue, green, red)
