import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('/Users/aadrita/python_codes/lesson8/image.jpeg')
i_rgb = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)

plt.imshow(i_rgb)
plt.title('Original Image')
plt.show()

gray_i = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_i, cmap = 'gray')
plt.title('Grayscale Image')
plt.show()

cropped_i = i[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_i, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title('Cropped Image')
plt.show()

(h, w) = i.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(i, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title('Rotated Image')
plt.show()

brightness_matrix = np.ones(i.shape, dtype="uint8") * 50
brighter = cv2.add(i, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title('Brighter Image')
plt.show()

cv2.imwrite('/Users/aadrita/python_codes/lesson8/gray_image.jpeg', gray_i)
cv2.imwrite('/Users/aadrita/python_codes/lesson8/cropped_image.jpeg', cropped_i)
cv2.imwrite('/Users/aadrita/python_codes/lesson8/rotated_image.jpeg', rotated)
cv2.imwrite('/Users/aadrita/python_codes/lesson8/brighter_image.jpeg', brighter)