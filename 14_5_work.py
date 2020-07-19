import cv2
import numpy as np
import matplotlib.pylab as plt

# img = cv2.imread('test10.jpg')
img = cv2.imread('139099.jpg')
rows, cols, ch = img.shape

# 四個角一開始的目標
markpoint = [[247, 225], [821, 335], [47, 1068], [1067, 1092]]
# 四個角結束的目標
dstpoint = [[0, 0], [1105, 0], [0, 1474], [1107, 1468]]

# 强调标记点
for i in markpoint:
    cv2.circle(img, tuple(i), 10, (0, 255, 0), -1)

# 转换点的格式
pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

# 生成透视矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 转换 以四個角的結束目標為主
dst = cv2.warpPerspective(img, M, (1107, 1468))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
