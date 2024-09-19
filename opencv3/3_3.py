#在OpenCV中实现一个画布，本质为创建一个指定大小的3维数组，并通过imshow函数显示出来，代码如下：
import cv2
import numpy as np
canvas = np.zeros((500, 500, 3), np.uint8)
cv2.imshow("canvas", canvas)
print(canvas[250,250])
cv2.waitKey()
