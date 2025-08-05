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

# 픽셀의 개수, 비율 리스트 작성
ratio_counts = []
number_counts = []
for i in range(len(center)):
    count = len(data[label.ravel()==i])
    number_counts.append(count)
    ratio_counts.append(count/data.shape[0])

# 색상 설정
colors = []
for i in range(len(center)):
    temp = [int(item)/255 for item in center[i]]
    colors.append(tuple(reversed(temp))) # BGR -> RGB 순서로 저장

xlist = [f'C{i}' for i in range(1, 17)]

# 결과 출력
plt.subplot(1,2,1)
plt.pie(ratio_counts, labels=xlist, autopct='%.1f%%')

plt.subplot(1,2,2)
plt.bar(xlist, ratio_counts, color=colors)

plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()