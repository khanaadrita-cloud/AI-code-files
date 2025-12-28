import cv2
import os

path = "/Users/aadrita/python_codes/lesson7/image.jpeg"
print("Exists:", os.path.exists(path))

i = cv2.imread(path)
print("Loaded:", i is not None)

gray_image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))
cv2.imshow('Processed Image', resized_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpeg', resized_image)
    print('Image saved as grayscale_resized_image.jpeg')
else:
    print('Image not saved')

cv2.destroyAllWindows()
print('Processed Image Dimensions', resized_image.shape)