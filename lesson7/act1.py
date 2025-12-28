import cv2
i = cv2.imread('/Users/aadrita/python_codes/lesson7/image.jpeg')
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)
cv2.imshow('Loaded Image', i)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('Image Dimensions', i.shape)