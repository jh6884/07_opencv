import numpy as np, cv2
import matplotlib.pyplot as plt

K = 16
img = cv2.imread('../img/load_line.jpg')
data = img.reshape((-1, 3)).astype(np.float32) 
# 데이터 평균을 구할 때 소수값 이하 점을 가질 수 있으므로 변환
# 반복 중지 조건
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# 평균 클러스터링 적용
ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# print(center)
zero = len(data[label.ravel()==0])
one = len(data[label.ravel()==1])
colors = []
for i in range(len(center)):
    colors.append(center[i].tolist())

print(colors)

# cv2.imshow('Image', img)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()