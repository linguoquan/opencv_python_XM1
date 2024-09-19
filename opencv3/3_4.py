# import cv2
# import numpy as np
# class Canvas:
#     def __init__(self):
#         self._win = 'canvas'
#         self._bar_value_red = 0
#         self._bar_value_green = 0
#         self._bar_value_blue = 0
#         self._bar_name_red = 'red'
#         self._bar_name_green = 'green'
#         self._bar_name_blue = 'blue'
#         self._canvas = np.zeros((500, 500, 3), np.uint8)
#
#
#     def _setBarConfig(self):
#         '''
#             滑动条初始化模块
#         '''
#
#         cv2.namedWindow(self._win)
#         cv2.createTrackbar(self._bar_name_red, self._win, 0, 255, self._callback)
#         cv2.createTrackbar(self._bar_name_green, self._win, 0, 255, self._callback)
#         cv2.createTrackbar(self._bar_name_blue, self._win, 0, 255, self._callback)
#
#     def _changeColor(self):
#         '''
#             画布背景颜色调整模块
#         '''
#         self._canvas[:] = (self._bar_value_blue, self._bar_value_green, self._bar_value_red)
#
#     def _callback(self, input):
#         '''
#             界面交互模块
#         '''
#         self._bar_value_red = cv2.getTrackbarPos(self._bar_name_red, self._win)
#         self._bar_value_green = cv2.getTrackbarPos(self._bar_name_green, self._win)
#         self._bar_value_blue = cv2.getTrackbarPos(self._bar_name_blue, self._win)
#         self._changeColor()
#
#
#     def run(self):
#         '''
#             画布显示模块
#         '''
#         self._setBarConfig()
#         cv2.imshow(self._win, self._canvas)
#         while True:
#             cv2.imshow(self._win, self._canvas)
#             if cv2.waitKey(1) == ord('q'):
#                 break


import cv2
import numpy as np


def nothing(x):
    # 回调函数
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows()