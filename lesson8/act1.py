import cv2
import matplotlib.pyplot as plt

i = cv2.imread("/Users/aadrita/python_codes/lesson8/image.jpeg")

i_rgb = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
plt.imshow(i_rgb)
plt.title('RGB Image')
plt.show()

gray_i = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_i, cmap='gray')
plt.title('Grayscale Image')
plt.show()

crop_i = i[100:300, 200:400]
crop_i_rgb = cv2.cvtColor(crop_i, cv2.COLOR_BGR2RGB)
plt.imshow(crop_i_rgb)
plt.title('Cropped Image')
plt.show()