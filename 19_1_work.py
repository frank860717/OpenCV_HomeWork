import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('20200603.png', 0)
edges = cv2.Canny(img, 0, 10)
edges2 = cv2.Canny(img, 0, 40)
edges3 = cv2.Canny(img, 170, 200)
edges4 = cv2.Canny(img, 130, 150)
edges5 = cv2.Canny(img, 200, 255)

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(232), plt.imshow(edges, cmap='gray'), plt.title('Edge Image')
plt.subplot(233), plt.imshow(edges2, cmap='gray'), plt.title('Edge Image')
plt.subplot(234), plt.imshow(edges3, cmap='gray'), plt.title('Edge Image')
plt.subplot(235), plt.imshow(edges4, cmap='gray'), plt.title('the best Image')
plt.subplot(236), plt.imshow(edges5, cmap='gray'), plt.title('Edge Image')

plt.show()
