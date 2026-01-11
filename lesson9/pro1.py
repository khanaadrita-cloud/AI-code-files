import cv2
import matplotlib.pyplot as plt
i = cv2.imread("/Users/aadrita/python_codes/lesson9/i1.jpeg")
i_rgb = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
h, w, _ = i.shape
a_start_left = (20, h - 50)
a_end_right = (w - 20, h - 50)
cv2.arrowedLine(i_rgb, a_start_left, a_end_right, (255, 0, 0), 3, tipLength=0.05)
cv2.arrowedLine(i_rgb, a_end_right, a_start_left, (255, 0, 0), 3, tipLength=0.05)
w_label_pos = (w // 2 - 100, h - 80)
cv2.putText(i_rgb, f'Width: {w}px', w_label_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imwrite('output_images/annotated_width.jpg', i_rgb)
plt.imshow(i_rgb)
plt.title('Annotated Image with Bi-Directional Width Arrows')
plt.axis('off')
plt.show()