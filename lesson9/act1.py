import cv2
import matplotlib.pyplot as plt

i = cv2.imread("/Users/aadrita/python_codes/lesson9/i1.jpeg")
i_rgb = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
h, w, _ = i_rgb.shape

sw, sh = 150, 150
top_left = (20, 20)
bottom_right = (top_left[0] + sw, top_left[1] + sh)
cv2.rectangle(i_rgb, top_left, bottom_right, (255, 0, 0), 3)

rw, rh = 200, 150
top_left_r = (w-rw-20, h-rh-20)
bottom_right_r = (top_left_r[0] + rw, top_left_r[1] + rh)
cv2.rectangle(i_rgb, top_left_r, bottom_right_r, (0, 255, 0), 3)

c1_x = top_left[0] + sw // 2
c1_y = top_left[1] + sh // 2
cv2.circle(i_rgb, (c1_x, c1_y), 15, (64, 75, 30), -1)
c2_x = top_left_r[0] + rw // 2
c2_y = top_left_r[1] + rh // 2
cv2.circle(i_rgb, (c2_x, c2_y), 15, (45, 27, 80), -1)

cv2.line(i_rgb, (c1_x, c1_y), (c2_x, c2_y), (0, 0, 255), 3)

cv2.putText(i_rgb, 'Region 1', (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(i_rgb, 'Region 2', (top_left_r[0], top_left_r[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(i_rgb, 'Center 1', (c1_x - 40, c1_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(i_rgb, 'Center 2', (c2_x - 40, c2_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

arrow_start = (w - 50, 20)
arrow_end = (w - 50, h - 20)

cv2.arrowedLine(i_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength = 0.05)
cv2.arrowedLine(i_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength = 0.05)

h_label_pos = (arrow_start[0] - 150, (arrow_start[1] - arrow_end[1]) // 2)
cv2.putText(i_rgb, f'Height: {h}px', h_label_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize = (12, 8))
plt.title('Annotated Image with Regions, Centers and bidirectional Arrow')
plt.imshow(i_rgb)
plt.axis('off')
plt.show()